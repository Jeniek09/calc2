"""absolute path for file locations"""
from pathlib import Path

class Abspath:
    """absolute path"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def absolutepath(filepath):
        """getting the absolute path for a file"""
        relative = Path(filepath)
        return relative.absolute()
