"""Index page Controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class IndexController(ControllerBase):
    """Class for Index page Controller"""
    @staticmethod
    def get():
        """Index page Controller"""
        return render_template('index.html')
