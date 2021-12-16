"""SOLID page Controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class SolidController(ControllerBase):
    """Class for SOLID page Controller"""
    @staticmethod
    def get():
        """SOLID page Controller"""
        return render_template('solid.html')
