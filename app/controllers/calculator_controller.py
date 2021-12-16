"""controller for the calculator operations"""
from datetime import date
import pandas as pd
# pylint: disable=unused-import
from flask import render_template, request, flash, redirect, url_for
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator


class CalculatorController(ControllerBase):
    """class for calculator controller"""
    @staticmethod
    def post():
        """class for calculator post operations"""
        if request.form['value1'] == '' and  request.form['value2'] != '':
            error = 'You must enter a value for value 1'
        elif request.form['value1'] != '' and  request.form['value2'] == '':
            error = 'You must enter a value for value 2'
        elif request.form['value1'] == '' and  request.form['value2'] == '':
            error = 'You must enter a value for value 1 and value 2'
        elif (request.form['value1'] == ' ' or request.form['value2'] == ' '):
            error = 'You must enter a value for value 1 or value 2'
        else:
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # this will call the correct operation
            getattr(Calculator, operation)(float(value1), float(value2))
            result = str(Calculator.get_last_result_value())
            df_csv = pd.DataFrame([[operation,float(value1),float(value2),float(result), str(date.today().strftime("%m/%d/%Y"))]]
                                    , columns=['Operation', 'Value_1', 'Value_2', 'Result','Date'])
            writefullpath = '/home/myuser/./app/controllers/output' + '/' + 'webcalc_output.csv'
            # df_csv.to_csv(writefullpath, header=True)
            df_csv.to_csv(writefullpath, mode='a', index=False, header=False)
            return render_template('output.html', value1=float(value1), value2=float(value2), operation=operation, result=result)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        """class for calculator get operations"""
        return render_template('calculator.html')
    