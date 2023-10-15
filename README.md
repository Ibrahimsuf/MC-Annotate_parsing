# MC-Annotate_parsing
Python script to parse the output of MC-Annotations and RNAVIEW annotations

You must download MC-Annotate(https://major.iric.ca/MajorLabEn/MC-Tools.html) and move it to this directory, as well as install and configure rna view(https://github.com/rcsb/RNAView)


The program runs MC Annotate and RNAVIEW on the pdb file and outputs a csv with all of the annotatons from both softwares

run with 
```bash
python main.py <rna filename>
