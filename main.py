from rna import RNA
import sys


def main():
    rna_file = sys.argv[1]

    rna = RNA(rna_file)
    rna.write_to_output_file("base_pairs")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("python main.py <rna filename>")