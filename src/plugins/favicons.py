import os
from shutil import copyfile


def postBuild(site):
    '''
    Copy the files from favicons to the build path root
    '''
    for root, _, paths in os.walk(os.path.join(site.path, "favicons")):
        for path in paths:
            copyfile(
                os.path.join(root, path),
                os.path.join(site.build_path, path)
            )
