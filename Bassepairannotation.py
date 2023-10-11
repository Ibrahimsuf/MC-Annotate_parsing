class BasePairAnnotation:
    def __init__(self) -> None:
        self.features = {}
        self.location = None
    
    def read_features_from_MCAnnotate_ouput(self, MCAnnotateoutput):
        #MCAnnotate_output is "R3-S16 : G-C Bs/Ww pairing antiparallel cis 128"
        print(MCAnnotateoutput.strip().split())
        self.location                                         = MCAnnotateoutput.strip().split()[0]
        self.features["Base-base interaction"]                = MCAnnotateoutput.strip().split()[2]
        self.features["Interacting edges"]                    = MCAnnotateoutput.strip().split()[3]
        self.features["Paired/Nonpaired"]                     = MCAnnotateoutput.strip().split()[4]
        self.features["Orientation around glycosidic bond"]   = MCAnnotateoutput.strip().split()[5]
        self.features["Relative glycosidic bond orientation"] = MCAnnotateoutput.strip().split()[6]

        if len(MCAnnotateoutput.strip().split()) == 8:
            self.features["MC-Sym number"]                    = MCAnnotateoutput.strip().split()[7]
        else:
            self.features["MC-Sym number"]                    = "N/A"
