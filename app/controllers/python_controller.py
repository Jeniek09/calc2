"""Python page Controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class PythonpgController(ControllerBase):
    """Class for Python page Controller"""
    @staticmethod
    def get():
        """Python page Controller"""
        return render_template('python.html')
