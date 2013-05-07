"""
Tools to alert New Relic of deploys
"""

from fabric.api import task

import urllib
import urllib2


from fabric_colors.environment import set_target_env

@task
def report_deploy():
    """
    Get the New Relic deploy XML. This records a deploy action with
    the New Relic monitoring tool.
    """
    deploy_url = "https://rpm.newrelic.com/deployments.xml"
