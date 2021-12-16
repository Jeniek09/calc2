"""Result page Controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class ResultController(ControllerBase):
    """Result page Controller"""
    @staticmethod
    def get():
        """Result page Controller"""
        return render_template('output.html')
