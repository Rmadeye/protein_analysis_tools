import os
from typing import Union

import pandas as pd

class USalign_parser:
    def __init__(self, usalign_output: Union[os.PathLike, str, pd.DataFrame]) -> None:
        # self.usalign_output = usalign_output
        # if isinstance(self.usalign_output, os.PathLike or str):

        #     assert os.path.exists(usalign_output), 'Invalid path or file does not exist'
            # load the file skipping each second line apart from first one
        self.usalign_output = pd.read_csv(usalign_output, sep='\s+', skiprows=lambda x: x % 2 != 0)


    def read_usalign_output(self):
        """
        Rename the paths to pdb names
        """
        # self.usalign_output['reference'] = self.usalign_output['reference'].str.split('/').str[-1]
        # self.usalign_output['target'] = self.usalign_output['target'].str.split('/').str[-1]
        return self.usalign_output
    

test = '/home/rmadeye/scripts/protein_analysis_tools/tools/usalign/usalign_output.txt'

print(USalign_parser(test).read_usalign_output())