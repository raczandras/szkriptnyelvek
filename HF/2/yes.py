#!/usr/bin/env python3
# encoding: utf-8

import sys


def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")

    if inp == 'y' or inp == 'Y' or inp == 'yes':    # <- eredeti
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')
    main()



    yes = set(['yes','y', 'Y'])
    if inp in yes:    # <- első ötletem
        print('bye')
        sys.exit(0)
    #for any other input:
    print('The show goes on...')
    main()



    if inp.lower() in ['yes', 'y']:    # <- második ötletem
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')
    main()

##############################################################################

if __name__ == "__main__":
    main()