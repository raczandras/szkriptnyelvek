#!/usr/bin/env python3

import sys

def main():
	if sys.argv[1].isdigit() and sys.argv[1].isdigit():
		szam1 = int(sys.argv[1])
		szam2 = int(sys.argv[2])
		print(szam1 + szam2)
	else:
		print('Ket darab szamot kérek argumentumként.')


if __name__ == "__main__":
	main()
