import subprocess
import os
from typing import Union

import os
import subprocess
from typing import Union


class RunUSAlign:
    def __init__(self, usalign_binary: Union[os.PathLike, str]) -> None:
        """
        Initialize the RunUSAlign object.

        Parameters:
            usalign_binary (Union[os.PathLike, str]): The path to the USAlign binary executable.

        Returns:
            None
        """
        self.usalign_binary = usalign_binary

    def run_usalign(
        self,
        reference_pdb: Union[os.PathLike, str],
        target_pdb: Union[os.PathLike, str],
        output_filename: str,
        mm=1,
        ter=0,
        outfmt=2,
        pymol=False,
        matrix=False,
        pdb_rank=None,
    ) -> int:
        """
        Run the USAlign program with the given parameters.

        Parameters:
            reference_pdb (Union[os.PathLike, str]): The path to the reference PDB file.
            target_pdb (Union[os.PathLike, str]): The path to the target PDB file.
            output_filename (str): The name of the output file to save the USAlign results.
            mm (int): The mm option for USAlign (default: 1).
            ter (int): The ter option for USAlign (default: 0).
            outfmt (int): The output format for USAlign results (default: 2).
            pymol (bool): Whether to generate a PyMOL session file (default: False).
            matrix (bool): Whether to generate a rotation matrix file (default: False).
            pdb_rank (Union[None, int]): The rank of the PDB file (default: None).

        Returns:
            int: 0 if the analysis ran successfully, 1 otherwise.
        """
        print(f"Processing {reference_pdb} with {target_pdb}...")

        target_pdb_parent_directory_path = (
            target_pdb_parent_directory
        ) = os.path.basename(target_pdb_parent_directory_path)

        assert isinstance(reference_pdb, str) and isinstance(
            target_pdb, str
        ), "Invalid path or file does not exist"

        if pymol == False:
            command = (
                f"{self.usalign_binary} {target_pdb} {reference_pdb} -mm {mm} -ter {ter} -outfmt {outfmt} -o "
                f"{os.path.join(target_pdb_parent_directory, f'usalign_{pdb_rank}.txt')} "
                f"-m {os.path.join(target_pdb_parent_directory, f'matrix_{pdb_rank}.dat')} "
                f">> {output_filename}"
            )

        if matrix == False:
            command = (
                f"{self.usalign_binary} {target_pdb} {reference_pdb} -mm {mm} -ter {ter} -outfmt {outfmt} -o "
                f"{os.path.join(target_pdb_parent_directory, f'usalign_{pdb_rank}.txt')}  "
                f"{os.path.join(target_pdb_parent_directory, f'usalign_pymol_{pdb_rank}.pse')} "
                f">> {output_filename}"
            )

        if pymol == False and matrix == False:
            command = (
                f"{self.usalign_binary} {target_pdb} {reference_pdb} -mm {mm} -ter {ter} -outfmt {outfmt} -o "
                f"{os.path.join(target_pdb_parent_directory, f'usalign_{pdb_rank}.dat')} "
                f">> {output_filename}"
            )

        if pymol == True and matrix == False:
            command = (
                f"{self.usalign_binary} {target_pdb} {reference_pdb} -mm {mm} -ter {ter} -outfmt {outfmt} -o "
                f"{os.path.join(target_pdb_parent_directory, f'usalign_pymol_{pdb_rank}.pse')} "
                f"-m {os.path.join(target_pdb_parent_directory, f'matrix_{pdb_rank}.dat')} "
                f">> {output_filename}"
            )

        result = subprocess.run(command, shell=True)

        if result.returncode == 0:
            print("Analysis ran successfully")
            return 0
        else:
            with open("usalign_errors.txt", "a+") as fout:
                print("Analysis encountered an error")
                fout.write(f"{reference_pdb} FAILED WITH {target_pdb}\n")
            return 1
