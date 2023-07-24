import subprocess
import os
from typing import Union

class RunUSAlign:
    def __init__(self, usalign_binary) -> None:
        self.usalign_binary = usalign_binary
        
    def run_usalign(self, reference_pdb: Union[os.PathLike, str], target_pdb: Union[os.PathLike,  str], output_filename: str,
                    mm = 1, ter = 0, outfmt = 2, pymol = False, matrix = False,
                     pdb_rank = Union[None, int], ) -> int:

        print(f"Processing {reference_pdb} with {target_pdb}...")

        target_pdb_parent_directory_path =target_pdb_parent_directory = os.path.basename(target_pdb_parent_directory_path)

        assert reference_pdb.isinstance(str) and target_pdb.isinstance(str), "Invalid path or file does not exist"

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
            with open('usalign_errors.txt', 'a+') as fout:
                print("Analysis encountered an error")
                fout.write(f"{reference_pdb} FAILED WITH {target_pdb}\n")
            return 1