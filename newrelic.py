"""
Tools to alert New Relic of deploys
"""

from fabric.api import task
from fabric.abort import abort

import urllib
import urllib2

DEPLOY_URL = 'https://rpm.newrelic.com/deployments.xml'


@task
def report_deploy(api_key, app_name='', application_id='', description='',
                  revision='', changelog='', user=''):
    """
    Records a deploy action with the New Relic monitoring tool.

    Args:
        api_key:
            A string containing your New Relic API key
        app_name:
            A string with the name of the application, found in the
            newrelic.yml file. One of app_name or application_id is required.
        application_id:
            A string  ID # of the application. One of app_name or
            application_id is required.
        description:
            An optional description. Text annotation for the deployment -
            notes for you
        revision:
            A string representing the revision number from your source control
            system (SVN, git, etc.)
        changelog:
            A string containing a list of changes for this deployment
        user:
            A string containing the name of the user/process that triggered
            this deployment
    """
    if not app_name and not application_id:
        abort('No New Relic app_name or application_id was provided. \
              One is required.')

    # Build deploy information disctionary
    if app_name:
        app_values = {'deployment[app_name]': app_name}
    else:
        app_values = {'deployment[application_id]': application_id}
    if description:
        app_values.update({'deployment[description]': description})
    if revision:
        app_values.update({'deployment[revision]': revision})
    if changelog:
        app_values.update({'deployment[changelog]': changelog})
    if user:
        app_values.update({'deployment[user]': user})

    # Send New Relic POST message
    try:
        request = urllib2.Request(DEPLOY_URL, urllib.urlencode(app_values))
        request.add_header('X-api-key', api_key)
        urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        print 'Our attempt to report to New Relic caused a HTTPError: ', e.code
        print e.headers
        print e.fp.read()
        abort()
