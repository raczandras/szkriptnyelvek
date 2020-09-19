#!/usr/bin/env python3

import sys

def ispalindrome(s):
    return s == s[::-1]

def main():
	print(ispalindrome(sys.argv[1]))

if __name__ == "__main__":
	main()
