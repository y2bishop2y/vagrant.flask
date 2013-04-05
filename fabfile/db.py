
from fabric.decorators import task
from fabric.context_managers import settings, hide
from fabric.colors import cyan
from utils import do 

config_file_path = 'db/alembic.ini'

@task
def build():
    """Initialise and migrate database to latest version. """
    print(cyan('\nFABRIC: updating database...'))


    #with settings (hide('warnings'), warn_only=True):
    #     do('venv/bin/alembic -c %s init db/postgresql' % config_file_path)
