import sys
import os

import pandas as pd

# Get the absolute path of the root directory of your project (one level up from 'tests' directory)
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(root_directory)

from tools.usalign import usalign_parser as ua


pass