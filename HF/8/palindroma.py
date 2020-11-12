#!/usr/bin/env python3


def palindromok(szam):
    if str(szam) != str(szam)[::-1]:
        return False

    buffer = []

    while szam >= 1:
        buffer.append(str(szam % 2))
        szam = szam // 2

    binaris = ''.join(buffer)

    if str(binaris) != str(binaris)[::-1]:
        return False
    else:
        return True


def main(): 
    osszeg = 0
    for i in range(1000000):
        if palindromok(i):
            osszeg += i

    print(osszeg)


if __name__ == "__main__":
    main()
