#!/usr/bin/env python3

def main():
    szoveg = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

    i = 0
    while i < len(szoveg):
        if szoveg[i] == "z":
            szoveg = szoveg[:i]+"b"+szoveg[i+1: ]
        elif szoveg[i] == "Z":
            szoveg = szoveg[:i]+"B"+szoveg[i+1: ]
        elif szoveg[i] == "y":
            szoveg = szoveg[:i]+"a"+szoveg[i+1: ]
        elif szoveg[i] == "Y":
            szoveg = szoveg[:i]+"A"+szoveg[i+1: ]
        elif szoveg[i] not in ['!', ':' , '\n', ' '] :
            c = ord(szoveg[i])
            szoveg = szoveg[:i]+chr(c+2)+szoveg[i+1:]
        i += 1
    print(szoveg)

if __name__ == "__main__":
	main()