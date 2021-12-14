"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.python_controller import PythonpgController
from app.controllers.glossary_controller import GlossaryController
from app.controllers.oop_controller import OopController
from app.controllers.aaa_controller import AaaController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = 'K-rFkm[|u11RgsuY'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/python", methods=['GET'])
def pythonpg_get():
    return PythonpgController.get()

@app.route("/glossary", methods=['GET'])
def glossary_get():
    return GlossaryController.get()

@app.route("/oop_principles", methods=['GET'])
def oop_get():
    return OopController.get()

@app.route("/aaa_testing", methods=['GET'])
def aaa_get():
    return AaaController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()
