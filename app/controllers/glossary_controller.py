"""Result page Controller"""
from flask import render_template
from app.controllers.controller import ControllerBase

class GlossaryController(ControllerBase):
    """Class for Result page Controller"""
    @staticmethod
    def get():
        """Glossary page get controller"""
        return render_template('glossary.html')
    