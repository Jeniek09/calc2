"""testing csv read and write operations on addition"""
import pandas as pd
import pytest
from calc.csvmanager.read import Read
from calc.csvmanager.write import Write
from calc.calculator import Calculator
from calc.history.calculations import Calculations

def test_read_addition_csv():
    """testing out read function to the test_data folder"""
    filename = 'addition.csv'
    path = 'tests/test_data'
    fullpath = path + '/' + filename
    df_1 = Read.read_df_from_csv(fullpath)
    # assert type(df_1) is pd.DataFrame
    assert isinstance(df_1, pd.DataFrame)

@pytest.fixture
def _clear_history():
    """clears history before test"""
    Calculations.clear_history()

def test_calculator_add(_clear_history):
    """testing the addition function of the Calculator"""
    # pylint: disable=unsubscriptable-object
    filename = 'addition.csv'
    path = 'tests/test_data'
    fullpath = path + '/' + filename
    df_1 = Read.read_df_from_csv(fullpath)
    for ind in df_1.index:
        assert Calculator.addition(df_1['value_1'][ind].round(decimals=4),
                                   df_1['value_2'][ind].round(decimals=4)).round(decimals=4) \
               == df_1['result'][ind].round(decimals=4)

def test_write_csv():
    """testing out write function to the test_data folder"""
    read_filename = 'addition.csv'
    write_filename = 'addition_output.csv'
    read_path = 'tests/test_data'
    write_path = 'tests/test_output'
    readfullpath = read_path + '/' + read_filename
    writefullpath = write_path + '/' + write_filename
    df_1 = Read.read_df_from_csv(readfullpath)
    df_1['output'] = Calculator.addition(df_1['value_1'], df_1['value_2']).round(decimals=4)
    df_2 = df_1[['value_1','value_2','output']].copy()
    Write.write_df_to_csv(writefullpath,df_2)
