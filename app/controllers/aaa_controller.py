"""AAA testing page Controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class AaaController(ControllerBase):
    """AAA testing page Controller"""
    @staticmethod
    def get():
        """AAA testing page Controller"""
        return render_template('aaa_testing.html')
