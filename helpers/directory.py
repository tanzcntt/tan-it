import os

from definitions import ROOT_DIR
from config import settings
# new folder/dir name

def create_output_dir(new_directory, input_data):

    # Parent Directory path
    # In case of Windows, "D:/"
    parent_directory = ROOT_DIR + '/' + settings['directory']['output'] + '/' + input_data  + '/image'

    # Setting the path for folder creation
    path = os.path.join(parent_directory, new_directory)

    # Handle the errors
    try:
        # Create the directory in the path
        os.makedirs(path, exist_ok = True)
        print("Directory %s Created Successfully" % new_directory)
    except OSError as error:
        print("Directory %s Creation Failed" % new_directory)
    return path