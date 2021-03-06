# PYTHON 2 code
from fabric.api import *


def deploy():
    freeze_folder = 'gh-pages'
    freeze_branch = 'gh-pages'

    message = raw_input("Enter a git commit message:  ")
    local("git add -A && git commit -m \"%s\"" % message)
    local("git push origin master")
    with prefix("source venv/bin/activate"):
        local("python freeze.py")
    with lcd(freeze_folder):
        local("git add -A && git commit -m \"%s\"" % message)
        local("git push origin %s" % freeze_branch)
