# if for some reason one cannot use  pyrosetta...

import os
import subprocess
from typing import Union, List
from enum import Enum


class RunRosetta:
    def __init__(self, rosetta_bin_directory: str) -> None:
        self.bin_dir = rosetta_bin_directory
        assert os.path.isdir(
            self.bin_dir
        ), f"Rosetta bin directory {self.bin_dir} does not exist"

    def run_fast_relax(
        self, pdb_file: str, out_file: str, extra_flags: str = ""
    ) -> None:
        """
        Run minimisation on a pdb file
        """
        assert os.path.isfile(pdb_file), f"PDB file {pdb_file} does not exist"
        assert not os.path.isfile(out_file), f"Output file {out_file} already exists"

        command = f"{self.bin_dir}/minimize.linuxgccrelease -s {pdb_file} -out:file:scorefile score_minim.sc -ignore_zero_occupancy false \
-relax:constrain_relax_to_start_coords -relax:default_repeats 5 -relax:ramp_constraints false -in:file:fullatom -ex1 -ex2 -nstruct 1 {extra_flags} -o {out_file}"
        subprocess.run(command, shell=True, check=True)

    def run_interface_analysis(
        self,
        pdb_file: str,
        out_file: str,
        interchain_interface: list,
        output_scorefile_path: str,
        extra_flags: str = "",
    ) -> None:
        """
        Run interface analysis on a pdb file
        """
        assert os.path.isfile(pdb_file), f"PDB file {pdb_file} does not exist"
        assert not os.path.isfile(out_file), f"Output file {out_file} already exists"

        command = f"{self.bin_dir}/InterfaceAnalyzer.linuxgccrelease -s {pdb_file} -o {out_file} -interface {'_'.join(interchain_interface)} -pack_separated {extra_flags} -out:file:score_only -out:file:scorefile {output_scorefile_path}"
        subprocess.run(command, shell=True, check=True)

    def run_residue_energy_breakdown_(
        self, pdb_file: str, out_file: str, extra_flags: str
    ) -> None:
        """
        Run decomposition on a pdb file
        """
        assert os.path.isfile(pdb_file), f"PDB file {pdb_file} does not exist"
        assert not os.path.isfile(out_file), f"Output file {out_file} already exists"

        command = f"{self.bin_dir}/residue_energy_breakdown.linuxgccrelease -s {pdb_file} -out:file:silent {out_file}_decomposition.out {extra_flags}"
        subprocess.run(command, shell=True, check=True)
