#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.elemek = []

    def ures(self):
        if len(self.elemek) == 0:
            return True
        else:
            return False

    def betesz(self, elem):
        self.elemek.append(elem)

    def kivesz(self):
        if len(self.elemek) == 0:
            return None
        else:
            return self.elemek.pop()

    def meret(self):
        return len(self.elemek)
    
    def __str__(self):
        lista = []

        for i in self.elemek:
            lista.append(str(i))

        szoveg = '[' + ' '.join(lista)
        return szoveg


    

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
    

if __name__ == "__main__":
    main()