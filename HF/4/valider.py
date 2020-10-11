#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    lista = [ c for c in text if c in chars]
    eredmeny = ''.join(lista)
    return lista
    

def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()