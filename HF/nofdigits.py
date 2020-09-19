#!/usr/bin/env python3
		
def main():
	szam1 = 2**256
	szam2 = 0

	while szam1 != 0:
		szam1 = szam1 // 10
		szam2 += 1
		
	print("A 2^256 szám",szam2,"darab számjegyből áll.")

if __name__ == "__main__":
	main()