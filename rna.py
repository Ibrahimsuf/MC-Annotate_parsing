import subprocess
from Bassepairannotation import BasePairAnnotation
import pandas as pd
class RNA:
    def __init__(self, pdb_file) -> None:
        self.name = pdb_file.split(".")[0]
        self.pdb_file = pdb_file
        self.MCAnnotate_output = None
        self.RNAVIEW_output = None
        self.MC_base_pair_annotations = {}
        self.RNAVIEW_base_pair_annotations = {}
        self.annotations = {}
        self.annotations_unpacked = {}

    def run_mc_annotate(self):
        command = ["./MC-Annotate", self.pdb_file]
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

            if result.stderr:
                print("Error output:")
                print(result.stderr)
            else:
                self.MCAnnotate_output =  result.stdout

            print("MC-Annotate completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running MC-Annotate: {e}")
    
    def run_RNAView(self):
        command = ["rnaview", self.pdb_file]
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

            rna_view_output_filename = f"{self.pdb_file}.out"
            self.RNAVIEW_output = RNA.get_file_contents(rna_view_output_filename)

            print("RNA View completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running MC-Annotate: {e}")

    
    def get_MC_base_pair_annotations(self):
        base_pair_info = RNA.get_lines_after(self.MCAnnotate_output, "Base-pairs")

        print(base_pair_info)
        for line in base_pair_info:
            #create an annotation object for each base_pair
            base_pair_annotation = BasePairAnnotation()
            base_pair_annotation.read_features_from_MCAnnotate_ouput(line)

            if base_pair_annotation.MClocation in self.annotations:
                self.annotations[base_pair_annotation.MClocation] = self.annotations[base_pair_annotation.MClocation].merge(base_pair_annotation)
            else:
                self.annotations[base_pair_annotation.MClocation] = base_pair_annotation
    
    def get_RNAVIEW_annotations(self):
        base_pair_info = RNA.get_lines_after(self.RNAVIEW_output, "BEGIN_base-pair", "END_base-pair")

        print(base_pair_info)
        for line in base_pair_info:
            base_pair_annotation = BasePairAnnotation()
            base_pair_annotation.read_features_from_RNAVIEW_ouput(line)

            if base_pair_annotation.RNAVIEW_location in self.annotations:
                self.annotations[base_pair_annotation.RNAVIEW_location].merge(base_pair_annotation)
            else:
                self.annotations[base_pair_annotation.RNAVIEW_location] = base_pair_annotation
    
    def write_base_pair_annotations_to_file(self):
        for key, annotation in self.annotations.items():
            self.annotations_unpacked[key] = annotation.features
        output_file_name = f"{self.name}.all_base_pair_annotations"
        pd.DataFrame(self.annotations_unpacked).to_csv(output_file_name)

    @staticmethod
    def get_lines_after(lines, heading_keyword, ending_keyword = None):
            lines_after_heading = []
            heading_found = False

            for line in lines:
                # Check if the heading_keyword is in the line
                if heading_keyword in line:
                    heading_found = True
                    continue

                if ending_keyword and ending_keyword in line:
                    break
                # If the heading has been found, add the line to the result
                if heading_found:
                    lines_after_heading.append(line)

            return lines_after_heading

    @staticmethod
    def get_file_contents(file_name):
        with open(file_name, "r") as file:
            return file.read()



        
