from rna import RNA

rna = RNA("example.pdb")

with open("5fj8rnaview.out", "r") as file:
    rna.RNAVIEW_output = file.readlines()

with open("annotations.txt", "r") as file:
    rna.MCAnnotate_output = file.readlines()


rna.get_MC_base_pair_annotations()
rna.get_RNAVIEW_annotations()
rna.write_base_pair_annotations_to_file()

