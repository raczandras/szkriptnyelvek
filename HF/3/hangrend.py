#!/usr/bin/env python3

import sys

MELY = 'aáoóuú'
MAGAS = 'eéiíöőüű'

def rend(word):
    me = False
    ma = False
    for c in word:
        if c in MELY:
            me = True
        elif c in MAGAS:
            ma = True
    
    if me and ma:
      return "vegyes"
    elif me:
      return "mély"
    elif ma:
      return "magas"
    else:
      return "semmilyen"

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "zrt"]

    for w in words:
        print(rend(w))


if __name__ == "__main__":
	main()
