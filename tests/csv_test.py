"""testing csv read and write operations by creating a dummy file and importing it"""
import os.path
import pandas as pd
from calc.csvmanager.write import Write
from calc.csvmanager.read import Read

def test_write_csv():
    """testing out write function to the test_data folder"""
    filename = 'csv_output.csv'
    path = 'tests/test_output'
    fullpath = path + '/' + filename
    name_dict = {
        'value1': ['1.0', '2.0', '3.0', '4.0'],
        'value2': ['1.0', '2.0', '3.0', '4.0'],
        'result': [2.0, 4.0, 6.0, 8.0]
    }
    # os.remove(fullPath)
    df_1 = pd.DataFrame(name_dict)
    Write.write_df_to_csv(fullpath,df_1)
    assert os.path.exists(fullpath)
def test_read_csv():
    """testing out read function to the test_data folder"""
    filename = 'csv_output.csv'
    path = 'tests/test_output'
    fullpath = path + '/' + filename
    df_1 = Read.read_df_from_csv(fullpath)
    # assert type(df_1) is pd.DataFrame
    assert isinstance(df_1,pd.DataFrame)
