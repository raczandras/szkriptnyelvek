#!/usr/bin/env python3

def main():
    lista = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    eredmeny = sorted(set(lista))
    print(eredmeny)

if __name__ == "__main__":
    main()