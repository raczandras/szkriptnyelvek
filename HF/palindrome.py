#!/usr/bin/env python3
import sys

#triviális módszer
def isTrivialPalindrome(s):
    return s == s[::-1]

def isIterativePalindrome(s):
    i = 0;
    j = -1
    while i < len(s):
    	if( s[i] != s[j] ):
    		return False
    	else:
    		i += 1
    		j -= 1
    return True

def isRecursivePalindrome(s):
	if len(s) == 0 or len(s) == 1:
		return True
	elif s[0] != s[len(s)-1]:
		return False
	else:
		return isRecursivePalindrome(s[1 : len(s)-1])
		
def main():
	print(isTrivialPalindrome(sys.argv[1]))
	print(isIterativePalindrome(sys.argv[1]))
	print(isRecursivePalindrome(sys.argv[1]))

if __name__ == "__main__":
	main()