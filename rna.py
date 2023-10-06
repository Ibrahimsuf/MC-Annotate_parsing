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
        try:
            # Run the command and capture the output
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

            if result.stderr:
                print("Error output:")
                print(result.stderr)
            else:
                return result.stdout

            print("MC-Annotate completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running MC-Annotate: {e}")
        

    def write_to_output_file(self, kind_of_annotation):
        output_filename = f"{self.rna_name}_{kind_of_annotation}.txt"
        self.annotations.write_base_pair_info_to_file(output_filename)