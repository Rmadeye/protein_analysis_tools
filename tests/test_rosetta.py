import sys
import os

import pandas as pd

# Get the absolute path of the root directory of your project (one level up from 'tests' directory)
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(root_directory)

from tools.rosetta import rosetta_parser  as pr


# Helper function to create a temporary Rosetta output file for testing

def test_rosetta_parser_from_path():
    # Create a temporary Rosetta output file for testing
    test_file = 'tests/data/test.sc'

    # Initialize RosettaParser from the temporary file
    parser = pr.RosettaParser(test_file)

    # Test read_dataframe method
    df = parser.read_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 23)
    assert "SCORE:" in df.columns
    assert "total_score" in df.columns

def test_rosetta_parser_from_dataframe():
    # Create a sample DataFrame for testing
    data = {
        "SCORE:": [0.000],
        "total_score": [0.247],
        "complex_normalized": [-8.763],
        "dG_cross": [-0.331],
        "dG_cross/dSASAx100": [141.699],
        "dG_separated": [5.359],
        "dG_separated/dSASAx100": [1663.068],
        "dSASA_hphobic": [2644.261],
        "dSASA_int": [981.194],
        "dSASA_polar": [22.000],
        "delta_unsatHbonds": [-0.044],
        "hbond_E_fraction": [8.000],
        "hbonds_int": [500.000],
        "nres_all": [103.000],
        "nres_int": [0.000],
        "packstat": [0.120],
        "per_residue_energy_int": [0.490],
        "sc_value": [-0.104],
        "side1_normalized": [-5.615],
        "side1_score": [0.366],
        "side2_normalized": [17.955],
        "side2_score": ["prot_0001"],
    }
    df = pd.DataFrame(data)

#     # Initialize RosettaParser from the DataFrame
    parser = pr.RosettaParser(df)

#     # Test read_dataframe method
    parsed_df = parser.read_dataframe()
    assert parsed_df.equals(df)


