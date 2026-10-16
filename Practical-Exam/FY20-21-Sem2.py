#DID UNDER TIMECRUNCH< DO NOT EXPECT PERFECT CODE
def dna_transcription_I(dna):
    rna = ""
    while len(dna) > 0:
        if dna[0] == "A":
            rna += "U"
        elif dna[0] == "G":
            rna += "C"
        elif dna[0] == "T":
            rna += "A"
        elif dna[0] == "C":
            rna += "G"
        dna = dna[1:]
    return rna

def dna_transcription_R(dna):
    if len(dna) < 1:
        return ""
    if dna[0] == "A":
        rna = "U"
    elif dna[0] == "G":
        rna = "C"
    elif dna[0] == "T":
        rna = "A"
    elif dna[0] == "C":
        rna = "G"
            
    return rna + dna_transcription_R(dna[1:])

def rna_segment(rna):
    start = False
    segment = ""
    base_len = 0
    i = 0
    while i < (len(rna)-1):
        base_len +=1
        codon = rna[i] + rna[i+1]
        if (codon == "UU" or codon == "UG") and start == False:
            segment += codon
            i += 1
            start = True
            base_len = 0
            
        elif (codon == "AC" or codon == "AA") and start == True and base_len == 1:
            segment += codon
            return segment
        elif start == True:
            segment += rna[i]
            
        if base_len == 2:
            base_len = 0
            
        i+=1
        
def poly_property(poly):
    acidic = basic = polar = npolar = 0
    
    c_acidic = ["F", "P", "Q"]
    c_npolar = ["L", "O"]
    c_basic = ["M", "C", "R", "A"]
    c_polar = ["S", "T", "Y"]
    
    while len(poly) > 0:
        tmp =  poly[0]
        if tmp in c_acidic:
            acidic += 1
        elif tmp in c_polar:
            polar += 1
        elif tmp in c_npolar:
            npolar += 1
        elif tmp in c_basic:
            basic += 1
            
        poly = poly[1:]
    
    if acidic == basic == polar == npolar == 0:
        return "Neutral"
    elif acidic > basic:
        return "Acidic"
    elif acidic < basic:
        return "Basic"
    elif polar > npolar:
        return "Polar"
    else:
        return "Neutral"
      
def auspicious_number(n, bad):
    x = 9
    y = 10
    numbers = 0
    
    if 0 in bad:
        y -= 1
        bad = bad[1:]
    
    while len(bad) > 0:
        x -= 1
        y -= 1
        bad = bad[1:]
        
    numbers = x * y ** (n - 1)
    
    return numbers
    
