"""
Tools to alert New Relic of deploys
"""

from fabric.api import task

import urllib
import urllib2


@task
def report_deploy(app_values):
    """
    Get the New Relic deploy XML. This records a deploy action with
    the New Relic monitoring tool.

    Args:
        A dictionary of the New Relic Parameters.
    """
    deploy_url = "https://rpm.newrelic.com/deployments.xml"
    app_values = urllib.urlencode(app_values)
    request = urllib2.Request(deploy_url, app_values)
    request.add_header('x-api-key', env.newrelic['API_KEY'])
    urllib2.urlopen(request)
