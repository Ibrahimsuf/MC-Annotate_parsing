from rna import RNA
import sys


def main():
    rna_file = sys.argv[1]

    rna = RNA(rna_file)
    rna.run_mc_annotate()
    rna.run_RNAView()
    rna.get_MC_base_pair_annotations()
    rna.get_RNAVIEW_annotations()

    print(rna.MCAnnotate_output)
    print(rna.RNAVIEW_output)
    print(rna.MC_base_pair_annotations)
    print(rna.RNAVIEW_base_pair_annotations)
    rna.write_base_pair_annotations_to_file()

    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("python main.py <rna filename>")