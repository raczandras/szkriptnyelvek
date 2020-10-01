#!/usr/bin/env python3

def main():
    #1
    inp = ['auto', 'villamos', 'metro']
    eredmeny = [ s.upper() + '!'  for s in inp]
    print("1:")
    print(eredmeny)
    print()

    #2
    inp = ['aladar', 'bela', 'cecil']
    eredmeny = [ s.capitalize() for s in inp]
    print("2:")
    print(eredmeny)
    print("")

    #3
    eredmeny = [ 0 for s in range(10)]
    print("3:")
    print(eredmeny)
    print()

    #4
    inp = list(range(1, 10+1))
    eredmeny = [ n*2 for n in inp]
    print("4:")
    print(eredmeny)
    print()

    #5
    inp = list(range(1, 10+1))
    eredmeny = [ int(s) for s in inp]
    print("5:")
    print(eredmeny)
    print("")

    #6
    inp = "1234567"
    eredmeny = [ int(s) for s in inp ]
    print("6: ")
    print(eredmeny)
    print()

    #7
    inp = 'The quick brown fox jumps over the lazy dog'
    eredmeny = [ len(s) for s in inp.split() ]
    print("7: ")
    print(eredmeny)
    print()

    #8
    inp = "python is an awesome language"
    eredmeny = [ w[0] for w in inp.split() ]
    print("8: ")
    print(eredmeny)
    print()

    #9
    inp = 'The quick brown fox jumps over the lazy dog'
    eredmeny = [ (w, len(w)) for w in inp.split() ]
    print("9: ")
    print(eredmeny)
    print()

    #10
    eredmeny = [ n for n in range(0, 10, 2)]
    print("10: ")
    print(eredmeny)
    print()

    #11
    eredmeny = [ n**2 for n in range(0, 20) if n**2 % 2 == 0]
    print("11: ")
    print(eredmeny)
    print()

    #12
    eredmeny = [ n**2 for n in range(0, 20) if str(n**2)[-1] == "4"]
    print("12: ")
    print(eredmeny)
    print()

    #13
    inp = [chr(n) for n in range(65, 90+1)]
    eredmeny = "".join(inp)
    print("13: ")
    print(eredmeny)
    print()

    #14
    inp = [' apple ', ' banana ', ' kiwi']
    eredmeny = [ w.replace(" ", "") for w in inp]
    print("14: ")
    print(eredmeny)
    print()

    #15
    inp = [1, 0, 1, 1, 0, 1, 0, 0]
    eredmeny = [ str(s) for s in inp]
    eredmeny = "".join(eredmeny)
    print("15: ")
    print(eredmeny)
    print()

#############################################################################

if __name__ == "__main__":
    main()
