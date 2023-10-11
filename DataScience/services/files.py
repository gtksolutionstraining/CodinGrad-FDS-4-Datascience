import os


def validate_file_path(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False