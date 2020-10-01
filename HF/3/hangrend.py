#!/usr/bin/env python3

import sys

MELY = 'aáoóuú'
MAGAS = 'eéiíöőüű'

def rend(word):
    me = False
    ma = False
    for c in word:
        if c in MELY:
            me = True
        elif c in MAGAS:
            ma = True
    
    if me and ma:
        print(word + ": vegyes")
    elif me:
        print(word + ": mély")
    elif ma:
        print(word + ": magas")

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]

    for w in words:
        rend(w)


if __name__ == "__main__":
	main()