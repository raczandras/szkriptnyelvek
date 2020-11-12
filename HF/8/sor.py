#!/usr/bin/env python3

class Sor:
    def __init__(self):
        self.elemek = []

    def ures(self):
        if len(self.elemek) == 0:
            return True
        else:
            return False

    def elso(self):
        if len(self.elemek) == 0:
            return None
        else:
            return str(self.elemek[0])

    def utolso(self):
        if len(self.elemek) == 0:
            return None
        else:
            return str(self.elemek[-1])

    def betesz(self, elem):
        self.elemek.append(elem)

    def kivesz(self):
        if len(self.elemek) == 0:
            return None
        else:
            return self.elemek.pop(0)

    def meret(self):
        return len(self.elemek)

    def urit(self):
        self.elemek = []
    
    def __str__(self):
        lista = []

        for i in self.elemek:
            lista.append(str(i))

        szoveg = '[' + ' '.join(lista)
        return szoveg
 

def main():
    s = Sor()        # üres sor létrehozása
    print(s)         # [
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s.elso())  # 1
    print(s.utolso())# 5
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(x)         # 1
    print(s)         # [4 5
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
    print(s.elso())  # None
    print(s.utolso())# None
    s.betesz(1)
    s.betesz(4)
    print(s.meret()) # 2
    s.urit()
    print(s.meret()) # 0
    
    

if __name__ == "__main__":
    main()