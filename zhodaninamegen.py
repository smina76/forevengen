from random import randint

def zhodaniname(maxsyllables=6):
	
    
    def basic():
        reddie1 = ["V", "V", "V", "CV", "CV", "CV"]
        reddie2 = ["VC", "VC", "VC", "CV", "CV", "CV"]
        reddie6 = ["VC", "VC", "VC", "CVC", "CVC", "CVC"]
        reddie4 = ["CVC", "CVC", "CVC", "CVC", "CVC", "CVC"]
        reddie5 = ["CVC", "CVC", "CVC", "CVC", "CVC", "CVC"]
        reddie6 = ["CVC", "CVC", "CVC", "CVC", "CVC", "CVC"]
        
        basicdie = [reddie1, reddie2, reddie6, reddie4, reddie5, reddie6]
        redroll = randint(1,6)
        whiteroll = randint(1,6)
        #print(redroll, whiteroll)
        return basicdie[redroll - 1][whiteroll - 1]
   
    def alternate():
        reddie1 = ["V", "V", "V", "CV", "CV", "CV"]
        reddie2 = ["CV", "CV", "CV", "CV", "CV", "CV"]
        reddie6 = ["VC", "VC", "VC", "VC", "VC", "VC"]
        reddie4 = ["CVC", "CVC", "CVC", "CVC", "CVC", "CVC"]
        reddie5 = ["CVC", "CVC", "CVC", "CVC", "CVC", "CVC"]
        reddie6 = ["CVC", "CVC", "CVC", "CVC", "CVC", "CVC"]
        
        basicdie = [reddie1, reddie2, reddie6, reddie4, reddie5, reddie6]
        redroll = randint(1,6)
        whiteroll = randint(1,6)
        #print(redroll, whiteroll)
        return basicdie[redroll - 1][whiteroll - 1]

    def consonant_initial():
        reddie1_1 = ["b", "b", "b", "b", "b", "bl"]
        reddie1_2 = ["bl", "bl", "br", "br", "br", "br"]
        reddie1_3 = ["br", "ch", "ch", "ch", "ch", "ch"]
        reddie1_4 = ["ch", "ch", "ch", "ch", "ch", "ch"]
        reddie1_5 = ["ch", "cht", "cht", "cht", "cht", "cht"]
        reddie1_6 = ["cht", "cht", "d", "d", "d", "d"]
   
        reddie2_1 = ["d", "d", "d", "d", "d", "dl"]
        reddie2_2 = ["dl", "dl", "dl", "dl", "dl", "dl"]
        reddie2_3 = ["dr", "dr", "dr", "dr", "dr", "f"]
        reddie2_4 = ["f", "f", "f", "f", "fl", "fl"]
        reddie2_5 = ["fl", "fr", "fr", "fr", "j", "j"]
        reddie2_6 = ["j", "j", "j", "j", "j", "jd"]
        

        reddie3_1 = ["jd", "jd", "jd", "jd", "k", "k"]
        reddie3_2 = ["k", "k", "k", "kl", "kl", "kr"]
        reddie3_3 = ["kr", "l", "l", "l", "m", "m"]
        reddie3_4 = ["n", "n", "n", "n", "n", "n"]
        reddie3_5 = ["n", "n", "p", "p", "p", "p"]
        reddie3_6 = ["p", "p", "p", "pl", "pl", "pl"]
        
        reddie4_1 = ["pl", "pl", "pl", "pl", "pr", "pr"]
        reddie4_2 = ["pr", "q", "q", "ql", "ql", "qr"]
        reddie4_3 = ["qr", "r", "r", "r", "r", "r"]
        reddie4_4 = ["s", "s", "s", "s", "s", "s"]
        reddie4_5 = ["s", "sh", "sh", "sh", "sh", "sh"]
        reddie4_6 = ["sh", "sh", "sht", "sht", "sht", "sht"]
        
        reddie5_1 = ["sht", "sht", "sht", "t", "t", "t"]
        reddie5_2 = ["t", "t", "st", "st", "st", "st"]
        reddie5_3 = ["st", "st", "st", "tl", "tl", "tl"]
        reddie5_4 = ["tl", "tl", "tl", "tl", "tl", "tl"]
        reddie5_5 = ["tl", "ts", "ts", "ts", "v", "v"]
        reddie5_6 = ["v", "v", "v", "vl", "vl", "vr"]
        
        reddie6_1 = ["vr", "y", "y", "y", "z", "z"]
        reddie6_2 = ["z", "z", "z", "zd", "zd", "zd"]
        reddie6_3 = ["zd", "zd", "zd", "zd", "zd", "zd"]
        reddie6_4 = ["zd", "zh", "zh", "zh", "zh", "zh"]
        reddie6_5 = ["zh", "zh", "zhd", "zhd", "zhd", "zhd"]
        reddie6_6 = ["zhd", "zhd", "zhd", "zhd", "zhd", "zhd"]
        
        
        basicdie = [[reddie1_1, reddie1_2, reddie1_3, reddie1_4, reddie1_5, reddie1_6]]
        basicdie.append([reddie2_1, reddie2_2, reddie2_3, reddie2_4, reddie2_5, reddie2_6])
        basicdie.append([reddie3_1, reddie3_2, reddie3_3, reddie3_4, reddie3_5, reddie3_6])
        basicdie.append([reddie4_1, reddie4_2, reddie4_3, reddie4_4, reddie4_5, reddie4_6])
        basicdie.append([reddie5_1, reddie5_2, reddie5_3, reddie5_4, reddie5_5, reddie5_6])
        basicdie.append([reddie6_1, reddie6_2, reddie6_3, reddie6_4, reddie6_5, reddie6_6])
        
        initroll = randint(0,5)
        redroll = randint(0,5)
        whiteroll = randint(0,5)
        return basicdie[initroll][redroll][whiteroll]
        
    def vowel():
        reddie1_1 = ["a", "a", "a", "a", "a", "a"]
        reddie1_2 = ["a", "a", "a", "a", "a", "a"]
        reddie1_3 = ["a", "a", "a", "a", "a", "a"]
        reddie1_4 = ["a", "a", "a", "a", "a", "a"]
        reddie1_5 = ["a", "a", "a", "a", "a", "a"]
        reddie1_6 = ["a", "a", "a", "a", "a", "a"]
   
        reddie2_1 = ["a", "a", "a", "a", "a", "a"]
        reddie2_2 = ["a", "a", "a", "a", "a", "a"]
        reddie2_3 = ["a", "e", "e", "e", "e", "e"]
        reddie2_4 = ["e", "e", "e", "e", "e", "e"]
        reddie2_5 = ["e", "e", "e", "e", "e", "e"]
        reddie2_6 = ["e", "e", "e", "e", "e", "e"]
        
        reddie3_1 = ["e", "e", "e", "e", "e", "e"]
        reddie3_2 = ["e", "e", "e", "e", "e", "e"]
        reddie3_3 = ["e", "e", "e", "e", "e", "e"]
        reddie3_4 = ["e", "e", "e", "e", "e", "e"]
        reddie3_5 = ["e", "e", "e", "e", "e", "e"]
        reddie3_6 = ["e", "e", "e", "i", "i", "i"]
        
        reddie4_1 = ["i", "i", "i", "i", "i", "i"]
        reddie4_2 = ["i", "i", "i", "i", "i", "i"]
        reddie4_3 = ["i", "i", "i", "i", "i", "i"]
        reddie4_4 = ["i", "i", "i", "i", "i", "i"]
        reddie4_5 = ["i", "i", "i", "i", "i", "i"]
        reddie4_6 = ["i", "i", "ia", "ia", "ia", "ia"]
        
        reddie5_1 = ["ia", "ia", "ia", "ia", "ia", "ia"]
        reddie5_2 = ["ia", "ia", "ia", "ia", "ia", "ia"]
        reddie5_3 = ["ia", "ia", "ia", "ia", "ia", "ia"]
        reddie5_4 = ["ia", "ia", "ia", "ia", "ia", "ia"]
        reddie5_5 = ["ie", "ie", "ie", "ie", "ie", "ie"]
        reddie5_6 = ["ie", "ie", "ie", "ie", "ie", "ie"]
        
        reddie6_1 = ["ie", "ie", "ie", "ie", "ie", "ie"]
        reddie6_2 = ["ie", "ie", "ie", "ie", "ie", "ie"]
        reddie6_3 = ["ie", "ie", "ie", "ie", "o", "o"]
        reddie6_4 = ["o", "o", "o", "o", "o", "o"]
        reddie6_5 = ["o", "o", "o", "o", "o", "o"]
        reddie6_6 = ["r", "r", "r", "r", "r", "r"]
        
        
        basicdie = [[reddie1_1, reddie1_2, reddie1_3, reddie1_4, reddie1_5, reddie1_6]]
        basicdie.append([reddie2_1, reddie2_2, reddie2_3, reddie2_4, reddie2_5, reddie2_6])
        basicdie.append([reddie3_1, reddie3_2, reddie3_3, reddie3_4, reddie3_5, reddie3_6])
        basicdie.append([reddie4_1, reddie4_2, reddie4_3, reddie4_4, reddie4_5, reddie4_6])
        basicdie.append([reddie5_1, reddie5_2, reddie5_3, reddie5_4, reddie5_5, reddie5_6])
        basicdie.append([reddie6_1, reddie6_2, reddie6_3, reddie6_4, reddie6_5, reddie6_6])
        
        initroll = randint(0,5)
        redroll = randint(0,5)
        whiteroll = randint(0,5)
        return basicdie[initroll][redroll][whiteroll]

    def consonant_final():
        reddie1_1 = ["b", "b", "bl", "bl", "bl", "bl"]
        reddie1_2 = ["bl", "bl", "bl", "br", "br", "br"]
        reddie1_3 = ["br", "br", "br", "br", "ch", "ch"]
        reddie1_4 = ["ch", "ch", "ch", "d", "d", "d"]
        reddie1_5 = ["d", "dl", "dl", "dl", "dl", "dl"]
        reddie1_6 = ["dl", "dl", "dr", "dr", "dr", "dr"]
   
        reddie2_1 = ["dr", "dr", "dr", "f", "f", "f"]
        reddie2_2 = ["f", "f", "fl", "fl", "fl", "fl"]
        reddie2_3 = ["fl", "fr", "fr", "fr", "fr", "fr"]
        reddie2_4 = ["j", "j", "j", "j", "k", "k"]
        reddie2_5 = ["kl", "kl", "kl", "kl", "kr", "kr"]
        reddie2_6 = ["l", "l", "l", "l", "l", "l"]
        

        reddie3_1 = ["l", "l", "l", "l", "l", "l"]
        reddie3_2 = ["m", "m", "m", "m", "nch", "nch"]
        reddie3_3 = ["nch", "nch", "nch", "nch", "nch", "nj"]
        reddie3_4 = ["nj", "nj", "nj", "nj", "ns", "ns"]
        reddie3_5 = ["ns", "ns", "ns", "nsh", "nsh", "nsh"]
        reddie3_6 = ["nsh", "nsh", "nsh", "nsh", "nt", "nt"]
        
        reddie4_1 = ["nt", "nt", "nts", "nts", "nts", "nts"]
        reddie4_2 = ["nz", "nz", "nz", "nz", "nz", "nzh"]
        reddie4_3 = ["nzh", "nzh", "nzh", "nzh", "nzh", "nzh"]
        reddie4_4 = ["p", "p", "pl", "pl", "pl", "pl"]
        reddie4_5 = ["pl", "pl", "pl", "pr", "pr", "pr"]
        reddie4_6 = ["pr", "pr", "pr", "pr", "q", "q"]
        
        reddie5_1 = ["ql", "ql", "qr", "qr", "r", "r"]
        reddie5_2 = ["r", "r", "r", "sh", "sh", "sh"]
        reddie5_3 = ["sh", "sh", "sh", "sh", "t", "t"]
        reddie5_4 = ["t", "t", "ts", "ts", "ts", "ts"]
        reddie5_5 = ["ts", "ts", "ts", "tl", "tl", "tl"]
        reddie5_6 = ["tl", "tl", "tl", "tl", "tl", "tl"]
        
        reddie6_1 = ["v", "v", "v", "v", "v", "vl"]
        reddie6_2 = ["vl", "vl", "vl", "vr", "vr", "vr"]
        reddie6_3 = ["vr", "vr", "z", "z", "z", "z"]
        reddie6_4 = ["z", "z", "z", "z", "z", "zh"]
        reddie6_5 = ["zh", "zh", "zh", "zh", "zh", "zh"]
        reddie6_6 = ["'", "'", "'", "'", "'", "'"]
        
        
        basicdie = [[reddie1_1, reddie1_2, reddie1_3, reddie1_4, reddie1_5, reddie1_6]]
        basicdie.append([reddie2_1, reddie2_2, reddie2_3, reddie2_4, reddie2_5, reddie2_6])
        basicdie.append([reddie3_1, reddie3_2, reddie3_3, reddie3_4, reddie3_5, reddie3_6])
        basicdie.append([reddie4_1, reddie4_2, reddie4_3, reddie4_4, reddie4_5, reddie4_6])
        basicdie.append([reddie5_1, reddie5_2, reddie5_3, reddie5_4, reddie5_5, reddie5_6])
        basicdie.append([reddie6_1, reddie6_2, reddie6_3, reddie6_4, reddie6_5, reddie6_6])
        
        initroll = randint(0,5)
        redroll = randint(0,5)
        whiteroll = randint(0,5)
        return basicdie[initroll][redroll][whiteroll]

        
    syllablecount = randint(1,maxsyllables)
    
    #print(f"Syllable Count: {syllablecount}")
    syllables = []
    
    for s in range(1, syllablecount+1):
        if s == 1:
            syllables.append(basic())
            #print(s, syllables[len(syllables)-1])
        else:
            if syllables[len(syllables)-1] == "V" or syllables[len(syllables)-1] == "CV":
                syllables.append(basic())
            else:
                syllables.append(alternate())
                
            #print(s, syllables[len(syllables)-1])
    
    #print(syllables)
    
    word=""
    
    for syllable in syllables:
        match syllable:
            case "V":
                word = word + vowel()
            case "CV":
                word = word + consonant_initial()
                word = word + vowel()
            case "VC":
                word = word + vowel()
                word = word + consonant_final()
            case "CVC":
                word = word + consonant_initial()
                word = word + vowel()
                word = word + consonant_final()
        
    return word.title()            
            
            
    
        
