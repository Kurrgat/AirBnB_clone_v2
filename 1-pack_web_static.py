#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder"""
    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive filename with current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the .tgz archive using tar command
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_path
    else:
        return None
