#!/usr/bin/python3
""" Generates a .tgz archive from the contents of the web_static folder
of AirBnB_clone repo """

from fabric.operations import local
from datetime import datetime


def do_pack():
    """ Function for file compression """
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result
