from fabric.decorators import task

import app
import db
import puppet
import virtualenv


@task
def build():
    """Execute build taks for all components."""
    virtualenv.build()
    db.build()


