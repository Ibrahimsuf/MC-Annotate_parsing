import re
class BasePairAnnotation:
    def __init__(self) -> None:
        self.features = {}
        self.MClocation = None
        self.RNAVIEW_location = None
    
    def read_features_from_MCAnnotate_ouput(self, MCAnnotateoutput):
        #MCAnnotate_output is "R3-S16 : G-C Bs/Ww pairing antiparallel cis 128"
        self.MClocation                                          = MCAnnotateoutput.strip().split()[0]
        self.features["MC-Base-base interaction"]                = MCAnnotateoutput.strip().split()[2].upper()
        self.features["MC-Interacting edges"]                    = MCAnnotateoutput.strip().split()[3]
        self.features["MC-Paired/Nonpaired"]                     = MCAnnotateoutput.strip().split()[4]
        self.features["MC-Orientation around glycosidic bond"]   = MCAnnotateoutput.strip().split()[5]
        self.features["MC-Relative glycosidic bond orientation"] = MCAnnotateoutput.strip().split()[6]

        if len(MCAnnotateoutput.strip().split()) == 8:
            self.features["MC-Sym number"]                    = MCAnnotateoutput.strip().split()[7]
        else:
            self.features["MC-Sym number"]                    = "n/a"
    
    def read_features_from_RNAVIEW_ouput(self, RNAVIEWoutput):
        #RNAVIEW output is "     3_36, R:     3 g-c    16 S: W/W cis    syn    n/a"

        RNAVIEWoutput = RNAVIEWoutput.strip()
        position_pattern = re.compile(r'(\d+)_(\d+)')

        position_match = re.search(position_pattern, RNAVIEWoutput)

        if position_match:
            self.features["position"] = position_match[0]

        location_letter_pattern = r'([A-Za-z]+):'

        location_number_pattern = r'-?\d+\.?\d*'
        location_numbers = re.findall(location_number_pattern, RNAVIEWoutput)


        location_letters = re.findall(location_letter_pattern, RNAVIEWoutput)

        base_pair_pattern = r'\b([A-Za-z])-([A-Za-z])\b'
        base_pair = re.findall(base_pair_pattern, RNAVIEWoutput)


       
        try:
            left_string, right_string = RNAVIEWoutput.split("/")[0:2]
            self.features["RNAVIEW-Interacting edges"] = f"{left_string.split()[-1]}/{right_string.split()[0]}"
        except:
            self.features["RNAVIEW-Interacting edges"] = None

        self.RNAVIEW_location = f"{location_letters[0]}{location_numbers[2]}-{location_letters[1]}{location_numbers[3]}"
        self.features["RNAVIEW-Base-base interaction"]  = f"{base_pair[0][0]}-{base_pair[0][1]}"
        self.features["RNAVIEW-MC-Sym number"] =  RNAVIEWoutput.split()[-1]

    def merge(self, other_annotation):
        self.features  = self.features | other_annotation.features


    def __str__(self) -> str:
        return str(self.features)
    
    def __repr__(self) -> str:
        return str(self.features)



