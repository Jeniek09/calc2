"""OOP page Controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class OopController(ControllerBase):
    """Class for OOP page Controller"""
    @staticmethod
    def get():
        """OOP Principles page Controller"""
        return render_template('oop_principles.html')
