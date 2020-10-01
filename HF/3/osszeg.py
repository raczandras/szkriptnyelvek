#!/usr/bin/env python3
import sys

def main():
    szam1 = 0
    szam2 = 0

    for i in range(1, 100+1):
        szam1 += i**2
        szam2 += i

    szam2 = szam2**2

    eredmeny = szam2 - szam1
    print("Száz számnál az eredmény: ", eredmeny)
    
if __name__ == "__main__":
	main()