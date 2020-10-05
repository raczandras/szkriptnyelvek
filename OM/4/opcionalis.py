#!/usr/bin/env python3

def ciklus(start, end, debug=False):
    if debug:
        print("# Ciklus kezdete")

    for i in range(start, end):
        print(i, end="")

    print()

    if debug:
        print("# Ciklus vége")

def main():
    ciklus(1,10, debug=True)
    print()
    ciklus(1,10)
   

#############################################################################

if __name__ == "__main__":
    main()
