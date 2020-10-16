#!/usr/bin/env python3

def isMun(szam):
    tarto = szam
    veg = 0

    while tarto != 0:
        if tarto % 10 != 0:
            veg += (tarto % 10)**(tarto % 10)
        tarto = tarto // 10

    return (veg == szam)

def main():
    for i in range(440000000):
        if( i % 1000000 == 0):
            print(i)
        if isMun(i):
           print(i)

            

#############################################################################
if __name__ == "__main__":
    main()
