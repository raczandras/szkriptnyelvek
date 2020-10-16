#!/usr/bin/env python3

def normalize( word ):
    word = word.replace(" ", "")
    word = word.lower()
    return word

def isAnagram( a,b ):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

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
