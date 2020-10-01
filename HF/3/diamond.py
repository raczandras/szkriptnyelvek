#!/usr/bin/env python3
import sys

def main():
    size = int(sys.argv[1])
    if size % 2 != 1:
        print("Páratlan számot kell megadni")
        sys.exit()

    i = 1
    while i < size:
        szoveg = "*"*i
        print(szoveg.center(size, " "), end="")
        print()
        i += 2

    while i > 0:
        szoveg = "*"*i
        print(szoveg.center(size, " "), end="")
        print()
        i -= 2

    

if __name__ == "__main__":
	main()