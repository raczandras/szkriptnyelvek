#!/usr/bin/env python3

from enum import Enum

class Beturendek(Enum):
    MELYHANGOK = 'aáoóuú'
    MAGASHANGOK = 'eéiíöőüű'


class Hangrendek(Enum):
    SEMMILYEN = 0
    MÉLY = 1
    MAGAS = 2
    VEGYES = 3


def hangrend(word):
    mely = False
    magas = False
    eredmeny = 0
    for c in word:
        if c in Beturendek.MELYHANGOK.value and not bool(mely):
            mely = True
            eredmeny += 1
        elif c in Beturendek.MAGASHANGOK.value and not bool(magas):
            magas = True
            eredmeny += 2
    return eredmeny


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "zrt"]

    for w in words:
        print( w + " -> " + Hangrendek(hangrend(w)).name ) 


if __name__ == "__main__":
	main()
