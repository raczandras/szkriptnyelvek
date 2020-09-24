#!/usr/bin/env python3
import sys	

def main():
	if len(sys.argv) < 3:
		print("Adjon meg két számot argumentumként a következő indításnál.")
	else:
		osszeg = int(sys.argv[1]) + int(sys.argv[2])
		print("A két megadott szám összege:",osszeg)


if __name__ == "__main__":
	main()