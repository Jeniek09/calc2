"""file utility for csv write"""
from calc.fileutils.absolutepath import Abspath

class Write:
    """write class for writing a csv output for the dataframe"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def write_df_to_csv(filename, df_1):
        """write class for writing a csv output for the dataframe"""
        return df_1.to_csv(Abspath.absolutepath(filename),float_format='%.4f', index=False, header=True)
