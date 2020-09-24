#!/usr/bin/env python3
#A sztring.count(szubsztring) függvény megszámolja azt, hogy egy adott sztringben hányszor fordul elő egy adott szubsztring.

def main():
	szoveg = "Négy meg négy meg nyolc meg négy az egyenlő húsz."
	print("Szöveg: " + szoveg)

	print('A "meg" szó', szoveg.count("meg"), 'alkalommal fordul elő a szövegben.')
	print('A "négy" szó kis kezdőbetűvel', szoveg.count("négy"), 'alkalommal fordul elő a szövegben.')
	print('A "Négy" szó nagy kezdőbetűvel', szoveg.count("Négy"), 'alkalommal fordul elő a szövegben.')

if __name__ == '__main__':
    main()