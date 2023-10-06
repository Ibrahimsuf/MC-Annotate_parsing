from annotations import Annotations
import sys


def main():
    annotations_filename = sys.argv[1]
    output_filename = sys.argv[2]

    annotations = Annotations(annotations_filename)
    annotations.write_base_pair_info_to_file(output_filename)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main()
    else:
        print("python main.py <annotations filename> <output filename>")