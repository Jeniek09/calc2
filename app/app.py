"""A simple flask web app"""
from flask import Flask
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController
from app.controllers.python_controller import PythonpgController
from app.controllers.glossary_controller import GlossaryController
from app.controllers.oop_controller import OopController
from app.controllers.aaa_controller import AaaController
from app.controllers.solid_controller import SolidController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.result_controller import ResultController

app = Flask(__name__)
app.secret_key = 'K-rFkm[|u11RgsuY'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    """calling Index page Controller"""
    return IndexController.get()

@app.route("/python", methods=['GET'])
def pythonpg_get():
    """calling Python page Controller"""
    return PythonpgController.get()

@app.route("/glossary", methods=['GET'])
def glossary_get():
    """calling Glossary page Controller"""
    return GlossaryController.get()

@app.route("/oop_principles", methods=['GET'])
def oop_get():
    """calling OOP page Controller"""
    return OopController.get()

@app.route("/aaa_testing", methods=['GET'])
def aaa_get():
    """calling AAA Testing page Controller"""
    return AaaController.get()

@app.route("/solid", methods=['GET'])
def solid_get():
    """calling SOLID page Controller"""
    return SolidController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """calling Calculator get Controller"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """calling Calculator post Controller"""
    return CalculatorController.post()

@app.route("/results", methods=['GET'])
def results_get():
    """calling Result page Controller"""
    return ResultController.get()
