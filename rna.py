import subprocess
from Bassepairannotation import BasePairAnnotation

class RNA:
    def __init__(self, pdb_file) -> None:
        self.name = pdb_file.split(".")[0]
        self.pdb_file = pdb_file
        self.MCAnnotate_output = None
        self.RNAVIEW_output = None
        self.MC_base_pair_Annotations = {}
        self.RNAVIEW_base_pair_Annotations = {}

    def run_mc_annotate(self):
        command = ["./MC-Annotate", self.pdb_file]
        try:
            # Run the command and capture the output
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
    
    def get_MC_base_pair_annotations(self):
        base_pair_info = get_lines_after(self.MC_base_pair_Annotations, "Base-pairs")

        for line in base_pair_info:
            #create an annotation object for each base_pair
            base_pair_annotation = BasePairAnnotation()
            base_pair_annotation.read_features_from_MCAnnotate_ouput(line)
            self.MC_base_pair_Annotations[base_pair_annotation.location] = base_pair_annotation
    
    def get_RNAVIEW_annotations(self):
        

def get_lines_after(lines, heading_keyword):
        lines_after_heading = []
        heading_found = False

        for line in lines:
            # Check if the heading_keyword is in the line
            if heading_keyword in line:
                heading_found = True
                continue
            # If the heading has been found, add the line to the result
            if heading_found:
                lines_after_heading.append(line)

        return lines_after_heading



        
