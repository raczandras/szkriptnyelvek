#!/usr/bin/env python3

def main():
    db = 0

    with open("jelmondatok.txt", "r") as f:
        for sor in f:
            sor = sor.rstrip('\n')
            lista = sor.split()
            if len(lista) == len(set(lista)):
                db += 1

    print(db)
    

if __name__ == "__main__":
    main()