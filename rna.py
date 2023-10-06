import subprocess
import re
from annotations import Annotations

class RNA:
    def __init__(self, rna_file) -> None:
        self.rna_file = rna_file
        self.annotations = Annotations(self.run_mc_annotate())
        self.rna_name = rna_file.split(".")[0]


    def run_mc_annotate(self):
        command = ["./MC-Annotate", self.rna_file]
        process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()

        if process.returncode == 0:
            return output
        else:
            print(f"Error: {error}")
            return None

    def write_to_output_file(self, kind_of_annotation):
        output_filename = f"{self.rna_name} {kind_of_annotation}"
        self.annotations.write_base_pair_info_to_file(output_filename)