# Fabric for deploying unobtrusify.com

from fabric.api import *

# SERVER
PRODUCTION = '46.51.184.117'


def production():
    """Production site"""
    env.alias = "production"
    env.hosts = [PRODUCTION]
    env.path = '/var/www/twittertickets.com'
    env.user = 'ubuntu'
    env.key_filename  = '/Users/phil.hawksworth/.ssh/philhawksworth-aws.pem'
    env.apache = 'twittertickets.com'
    env.release_path = "/var/releases/twittertickets.com"


def deploy():
    """Deployment actions"""
    export_release()
    

def export_release():
    """Exports a release with the current time and date"""
    run('cd %s && git pull origin master' % env.release_path)
    run('cp -R %(release_path)s/www/* %(path)s' % env)


def copy_apache():
    """Copies the apache file to the appropriate location."""
    command = 'cp %(release_path)s/etc/apache2/%(apache)s /etc/apache2/sites-available/'
    sudo(command % env)


def restart():
    """Restarts the apache server"""
    copy_apache()
    sudo('/etc/init.d/apache2 restart')
