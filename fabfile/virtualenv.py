
from fabric.decorators import task 
from fabric.context_managers import settings, hide
from fabric.colors import cyan, red
from fabric.utils import abort
from utils import do


@task
def build():
    """
    Build or update the virtualenv.
    """
    with settings(hide('stdout')):
        
        print(cyan('\nFABRIC: Updating venv, installing packages ...'))
        
        do('[-e venv] || virtualenv venv --no-site-packages') 


        with settings(warn_only=True):
            pip = do('venv/bin/pip install -r requirements.txt', capture=True)

        if pip.failed:
            print(red(pip))
            abort("pip exited with return code %i" % pip.return_code)
