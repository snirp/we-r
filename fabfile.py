# PYTHON 2 code
from fabric.api import *


def deploy():
    freeze_folder = 'gh-pages'
    freeze_branch = 'gh-pages'

    with prefix("source venv/bin/activate"):
        message = raw_input("Enter a git commit message:  ")
        local("git add -A && git commit -m \"%s\"" % message)
        local("git push origin master")
        local("python freeze.py")
        with cd(freeze_folder):
            local("git checkout %s" % freeze_branch)
            local("git add -A && git commit -m \"%s\"" % message)
            local("git push origin %s" % freeze_branch)
