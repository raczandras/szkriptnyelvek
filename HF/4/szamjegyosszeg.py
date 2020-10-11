#!/usr/bin/env python3

def main():
    lista = [str(i) for i in range(1,100+1)]
    szoveg = ''.join(lista)
    lista = list(szoveg)
    osszeg = 0

    for s in lista:
        osszeg += int(s)

    print(osszeg)

#############################################################################

if __name__ == "__main__":
    main()
