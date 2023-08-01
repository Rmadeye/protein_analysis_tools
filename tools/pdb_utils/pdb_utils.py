import os
from typing import Union

from biopandas.pdb import PandasPdb
import numpy as np

class PDBUtils:

    def __init__(self, pdb_file: Union[os.PathLike, str]) -> None:
        assert os.path.exists(pdb_file), f"{pdb_file} does not exist."

    def calculate_distance_between_residues(self, residue1: str, residue2: str, ligand = False) -> float:
        """
        Calculate the distance between two residues.

        Parameters:
            residue1 (str): The first residue.
            residue2 (str): The second residue or ligand

        Returns:
            float: The distance between the two residues.
        """
        pdb = PandasPdb().read_pdb(self.pdb_file)
        residue1 = pdb.df['ATOM'][pdb.df['ATOM']['residue_name'] == residue1]
        if ligand:
            residue2 = pdb.df['HETATM'][pdb.df['HETATM']['residue_name'] == residue2]
        else:
            residue2 = pdb.df['ATOM'][pdb.df['ATOM']['residue_name'] == residue2]
        distance = np.linalg.norm(residue1 - residue2)
        return distance
    
    def calculate_distance_between_atoms(self, atom1: str, atom2: str, ligand = False) -> float:
        """
        Calculate the distance between two atoms.

        Parameters:
            atom1 (str): The first atom.
            atom2 (str): The second atom of protein or ligand.

        Returns:
            float: The distance between the two atoms.
        """
        pdb = PandasPdb().read_pdb(self.pdb_file)
        atom1 = pdb.df['ATOM'][pdb.df['ATOM']['atom_name'] == atom1]
        if ligand:
            atom2 = pdb.df['HETATM'][pdb.df['HETATM']['atom_name'] == atom2]
        else:
            atom2 = pdb.df['ATOM'][pdb.df['ATOM']['atom_name'] == atom2]
        distance = np.linalg.norm(atom1 - atom2)
        return distance
    
    def truncate_structure_to_backbone(self):
        """
        Truncate the structure to only include the backbone atoms.

        Returns:
            PandasPdb: The truncated structure.
        """
        pdb = PandasPdb().read_pdb(self.pdb_file)
        pdb.df['ATOM'] = pdb.df['ATOM'][pdb.df['ATOM']['atom_name'].isin(['N', 'CA', 'C', 'O'])]
        return pdb
    
    def truncate_structure_by_residue_indices(self, end: int, start:  int=1, chain: str = 'A'):
        """
        Truncate the structure to only include the backbone atoms.

        Parameters:
            start (int): The start residue index.
            end (int): The end residue index.
            chain (str): The chain ID.

        Returns:
            PandasPdb: The truncated structure.
        """
        pdb = PandasPdb().read_pdb(self.pdb_file)
        pdb.df['ATOM'] = pdb.df['ATOM'][(pdb.df['ATOM']['residue_number'] >= start) & (pdb.df['ATOM']['residue_number'] <= end) & (pdb.df['ATOM']['chain_id'] == chain)]
        return pdb
    
    
    