#!/usr/bin/env python3
import sys

def product(li):
    p = 1
    for sz in li:
        p *= sz
    
    return p

def main():
    li1 = []
    print(product(li1))

    li2 = [1, 2]
    print(product(li2))

    li3 = [5, 4, 3, 2, 1]
    print(product(li3))

if __name__ == "__main__":
	main()