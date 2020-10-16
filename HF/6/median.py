#!/usr/bin/env python3

def getMedian( lista ):
    lista.sort()
    
    if len(lista) % 2 == 1:
        return lista[len(lista)// 2]
    else:
        a = lista[len(lista)// 2]
        b = lista[len(lista)//2 - 1]
        return (a+b)/2

def main():
    print("[1, 2, 3, 4, 5] =", getMedian([1, 2, 3, 4, 5]))
    print("[3, 1, 2, 5, 3] =", getMedian([3, 1, 2, 5, 3]))
    print("[1, 300, 2, 200, 1] =", getMedian([1, 300, 2, 200, 1]))
    print("[3, 6, 20, 99, 10, 15] =", getMedian([3, 6, 20, 99, 10, 15]))
    
#############################################################################

if __name__ == '__main__':
    main()
