#!/usr/bin/env python3

import sys

MELYHANGOK = 'aáoóuú'
MAGASHANGOK = 'eéiíöőüű'
EREDMENYEK = ["Semmilyen", "Mély", "Magas", "Vegyes"]


def rend(word):
    me = False
    ma = False
    eredmeny = 0
    for c in word:
        if c in MELYHANGOK and not bool(me):
            me = True
            eredmeny += 1
        elif c in MAGASHANGOK and not bool(ma):
            ma = True
            eredmeny += 2
    return eredmeny


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "zrt"]

    for w in words:
        print(EREDMENYEK[rend(w)])

if __name__ == "__main__":
	main()
