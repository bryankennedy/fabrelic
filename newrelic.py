"""
Tools to alert New Relic of deploys
"""

from fabric.api import task

import urllib
import urllib2


@task
def report_deploy(api_key, app_values):
    """
    Get the New Relic deploy XML. This records a deploy action with
    the New Relic monitoring tool.

    Args:
        api_key:
            A string containing your New Relic API key
        app_values:
            A dictionary containing the New Relic deploy parameters.
    """
    try:
        deploy_url = 'https://rpm.newrelic.com/deployments.xml'
        request = urllib2.Request(deploy_url, urllib.urlencode(app_values))
        request.add_header('X-api-key', api_key)
        urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        print 'Our attempt to report to New Relic caused a HTTPError: ', e.code
        print e.headers
        print e.fp.read()
