# MC-Annotate_parsing
Python script to parse the output of MC-Annotations

You must download MC-Annotate(https://major.iric.ca/MajorLabEn/MC-Tools.html) and move it to this directory, as well as install and configure rna view(https://github.com/rcsb/RNAView)


The program runs MC-Annotate on the specified .pdb file, and writes to a file with the list of base pairs and annotations


run with 
```bash
python main.py <rna filename>
