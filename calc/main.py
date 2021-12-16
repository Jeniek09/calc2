""" This is the main run file for pytest"""
import sys
import time
from datetime import date
import pytest

now = int(time.time())
file_name = f"logfile_{now}.xml"

class MyPlugin:
    """ This is the class docstring"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def pytest_sessionfinish():
        """ This is the sessionfinish docstring"""
        print("*** test run reporting finishing")
        print(file_name)
        today = date.today()
        print("Today date is: ", today)

if __name__ == "__main__":
    sys.exit(pytest.main(["-qq","-vv","--log-level=INFO","--junit-xml=/home/myuser/tests/logfile/"+file_name], plugins=[MyPlugin()]))
