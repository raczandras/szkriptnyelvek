#!/usr/bin/env python3
import sys
		
def main():
	szam1 = int(sys.argv[1])
	szam2 = 0

	while szam1 != 0:
		szam2 = szam2 * 10 + szam1 % 10
		szam1 = szam1 // 10
		
	print(szam2)

if __name__ == "__main__":
	main()