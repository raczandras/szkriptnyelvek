#!/usr/bin/env python3

MELYHANGOK = 'aáoóuú'
MAGASHANGOK = 'eéiíöőüű'
EREDMENYEK = ["Semmilyen", "Mély", "Magas", "Vegyes"]


def hangrend(word):
    mely = False
    magas = False
    eredmeny = 0
    for c in word:
        if c in MELYHANGOK and not bool(mely):
            mely = True
            eredmeny += 1
        elif c in MAGASHANGOK and not bool(magas):
            magas = True
            eredmeny += 2
    return eredmeny


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "zrt"]

    for w in words:
        print( w + " -> " + EREDMENYEK[hangrend(w)])

if __name__ == "__main__":
	main()
