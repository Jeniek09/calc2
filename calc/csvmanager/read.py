"""file utility for csv read"""
import pandas as pd
from calc.fileutils.absolutepath import Abspath

class Read:
    """read class for writing a csv output for the dataframe"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def read_df_from_csv(filename):
        """read class for writing a csv output for the dataframe"""
        return pd.read_csv(Abspath.absolutepath(filename))
