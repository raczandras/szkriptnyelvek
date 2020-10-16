#!/usr/bin/env python3



def main():
    szam = 2**1000
    szamjegyek = list(str(szam))
    osszeg = 0

    for c in szamjegyek:
        osszeg += int(c)

    print(osszeg)
    
#############################################################################

if __name__ == '__main__':
    main()
