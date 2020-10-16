#!/usr/bin/env python3

def normalize( word ):
    word = word.replace(" ", "")
    word = word.lower()
    return word

def isAnagram( a,b ):
    szo = {}
    if len(a) != len(b):
        return False
    
    for c in a:
        if c not in szo.keys():
            szo[c] = 0
        szo[c] += 1

    for c in b:
        if c not in szo.keys() or szo[c] == 0:
            return False
        szo[c] -= 1
    
    return True

def main():
    szavak = {}
    szavak["listen"] = "silent"
    szavak["A gentleman"] = "Elegant man"
    szavak["dormitory"] = "dirty room"
    szavak["alma"] = "lama"
    szavak["agy"] = "ggya"

    for k in szavak.keys():
        print( k ,"=", szavak[k], "->", isAnagram( normalize( k ), normalize( szavak[k] ) ))
    
#############################################################################

if __name__ == '__main__':
    main()
