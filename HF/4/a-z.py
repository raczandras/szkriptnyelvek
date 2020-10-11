#!/usr/bin/env python3
import sys

def main():
    if sys.argv[0] == "./a-z.py":
        elemek = [chr(i) for i in range(97, 122+1)]
    elif sys.argv[0] == "./z-a.py":
        elemek = [chr(i) for i in range (122, 97-1, -1)]
        
    szoveg = ''.join(elemek)
    print(szoveg)

#############################################################################
if __name__ == "__main__":
    main()