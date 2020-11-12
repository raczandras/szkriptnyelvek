#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.elemek = []

    def betesz(self, elem):
        self.elemek.append(elem)

    def kivesz(self):
        if len(self.elemek) == 0:
            return None
        else:
            return self.elemek.pop()

    def meret(self):
        return len(self.elemek)
    
    def sztringkent(self):
        lista = []

        for i in self.elemek:
            lista.append(str(i))

        szoveg = '[' + ' '.join(lista)
        return szoveg
    

class Sor:
    def __init__(self):
        self.foverem = Verem()
        self.bufferverem = Verem() 

    def is_empty(self):
        if self.foverem.meret() == 0:
            return True
        else:
            return False

    def append(self, elem):
        self.foverem.betesz(elem)

    def popleft(self):
        if self.foverem.meret() == 0:
            return None
        else:
            while self.foverem.meret() != 1:
                self.bufferverem.betesz(self.foverem.kivesz())

            ertek=self.foverem.kivesz()

            while self.bufferverem.meret() != 0:
                self.foverem.betesz(self.bufferverem.kivesz())
                
            return ertek

    def size(self):
        return self.foverem.meret()
    
    def __str__(self):
        return self.foverem.sztringkent()
 

def main():
    s = Sor()             #Üres sor
    print(s)              # [
    print(s.is_empty())   # True
    print(s.size())       # 0
    s.append(1)           
    s.append(4)
    s.append(5)

    print(s.is_empty())   # False
    print(s.size())       # 3

    x = s.popleft()
    print(x)              # 1

    s.popleft()
    s.popleft()
    x = s.popleft()
    print(x)              # None
   

if __name__ == "__main__":
    main()