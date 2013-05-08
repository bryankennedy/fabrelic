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
        A dictionary of the New Relic Parameters.
    """
    deploy_url = 'https://rpm.newrelic.com/deployments.xml'
    request = urllib2.Request(deploy_url, urllib.urlencode(app_values))
    request.add_header('X-api-key', api_key)
    response = urllib2.urlopen(request)
