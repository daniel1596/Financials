from pathlib import Path
from shutil import copyfile


class FileHelper:
    """Helper class for some basic file operations.
    They are all static/classmethods... the downsides of OOP I guess?"""

    @staticmethod
    def copy_file(old_path: str, new_path: str):
        copyfile(old_path, new_path)

    @classmethod
    def create_file(cls, path: str):
        if not Path(path).parent.exists():
            pass
            # Path(path).parent.mkdir() # doesn't work

        with open(path, 'w'):
            pass

        cls.ensure_file_exists(path)

    @classmethod
    def ensure_file_exists(cls, path: str):
        if not Path(path).exists():
            raise IOError("An error occurred when attempting to access the file.")
