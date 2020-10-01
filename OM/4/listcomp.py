#!/usr/bin/env python3

def main():
    #1
    inp = ['auto', 'villamos', 'metro']
    eredmeny = [ s.upper() + '!'  for s in inp]
    print(eredmeny)

    #2
    inp = ['aladar', 'bela', 'cecil']
    eredmeny = [ s.capitalize() for s in inp]
    print(eredmeny)

    #3
    eredmeny = [ 0 for s in range(10)]
    print(eredmeny)

    #4
    inp = list(range(1, 10+1))
    eredmeny = [ n*2 for n in inp]
    print(eredmeny)

    #5
    inp = list(range(1, 10+1))
    eredmeny = [ int(s) for s in inp]
    print(eredmeny)

    #6
    inp = "1234567"
    eredmeny = [ int(s) for s in inp ]
    print(eredmeny)

    #7
    inp = list(str.split('The quick brown fox jumps over the lazy dog'))
    eredmeny = [ len(s) for s in inp ]
    print(eredmeny)

    #8
    



#############################################################################

if __name__ == "__main__":
    main()
