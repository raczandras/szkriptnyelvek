#!/usr/bin/env python3
import sys

def main():
    print(sum([n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0 ]))
    

if __name__ == "__main__":
	main()