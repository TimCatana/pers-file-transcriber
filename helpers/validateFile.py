import os.path
from constants.constants import VALID_EXTENSIONS


# Makes sure the file is a valid audio file
def validateFileExtension(file):
    extension = os.path.splitext(file)[1]

    if (extension in VALID_EXTENSIONS):
        return True
    else:
        return False
