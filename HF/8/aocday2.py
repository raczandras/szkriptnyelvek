#!/usr/bin/env python3

def main():
    db = 0

    with open("tablazat.txt", "r") as f:
        osszeg = 0
        for sor in f:
            sor = sor.rstrip('\n')
            lista = sor.split('\t')
            lista = [ int(w) for w in lista]
            reszosszeg = max(lista) - min(lista)
            osszeg += reszosszeg

        print(osszeg)


if __name__ == "__main__":
    main()
