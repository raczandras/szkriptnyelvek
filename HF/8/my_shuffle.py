#!/usr/bin/env python3
import random

def shuffled(li):
    lista = li[0:len(li)]
    random.shuffle(lista)

    return lista


def main(): 
    lista = [3, 8, 2, 8, 4, 2, 1, 9]
    x = shuffled(lista)[0:5]

    print("összekevert lista(részlet): " + str(x))
    print("Eredeti lista: " + str(lista))
    


if __name__ == "__main__":
    main()
