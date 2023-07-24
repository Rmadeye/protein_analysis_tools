import os
import typing

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class RosettaParser:
    """
    Class to parse rosetta output files
    """

    def __init__(self, user_input: typing.Union[os.PathLike, pd.DataFrame]):

        if isinstance(user_input, pd.DataFrame):
            self.df = user_input

        elif isinstance(user_input, str):

            assert os.path.exists(path), 'Invalid path  or file does  not exist'

            with open(path, 'r') as f:
                if f.readline().split()[0] == 'SEQUENCE:':
                    self.df = pd.read_csv(path, sep='\s+', skiprows=1)
                    f.close()
                else:
                    self.df = pd.read_csv(path, sep='\s+')
                    f.close()
            assert self.df.shape[0] > 0, 'Empty dataframe'

    def read_dataframe(self):
        return self.df

    def get_top_n_by_selected_column(self, column: str, n: int = 10):
        return self.df.sort_values(by=column, ascending=False).head(n)
    
    def add_column_to_dataframe(self, column: str, values: typing.Union[typing.List, str, float, int]):
        self.df[column] = values
    
    def change_strings_in_selected_column_by_user_input(self, column: str, original: typing.Union[str, int, float],  replacement: str):
        if original == 'all':
            self.df[column] = replacement
        else:
            self.df[column] = self.df[column].str.replace(original, replacement)
    
    def plot_top_n_by_selected_column(self, column: str, n: int = 10):
        top_n = self.get_top_n_by_selected_column(column, n)
        sns.barplot(x=top_n['description'], y=top_n[column])
        plt.xticks(rotation=90)
        plt.show()

    def plot_histogram(self, column: str):
        sns.histplot(self.df[column])
        plt.show()

    

    
    


if __name__ == '__main__':
    path = '/home/rmadeye/scripts/protein_analysis_tools/tools/rosetta/interface.sc'
    r = RosettaParser(path)
    r_2 = RosettaParser(r.df)
    r_2.add_column_to_dataframe('nres_alla', 'abba')
    r_2.change_strings_in_selected_column_by_user_input('nres_alla', 'ab','dupa')
    print(r_2.read_dataframe().nres_alla)