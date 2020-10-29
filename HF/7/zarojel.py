#!/usr/bin/env python3

def helyesZarojel(szoveg):
    lista = []
    buffer = []
    
    jelek = {}
    jelek['('] = ')'
    jelek['['] = ']'
    jelek['{'] = '}'

    for c in szoveg:
        if c in ['(', '[', '{', ')', ']', '}']:
            lista.append(c)
    
    szoveg = ''.join(lista)

    for c in szoveg: 
        if c in ["(", "{", "["]: 
            buffer.append(c) 
        else: 
            if len(buffer) == 0: 
                return False

            utolso = buffer.pop() 

            if jelek[utolso] != c: 
                return False

    if len(buffer) != 0: 
        return False
    else:
        return True
    

def main():
    print(helyesZarojel("((5+3)*2+1)"))
    print(helyesZarojel("{[(3+1)+2]+}"))
    print(helyesZarojel("(3+{1-1)}"))
    print(helyesZarojel("[1+1]+(2*2)-{3/3}"))
    print(helyesZarojel("(({[(((1)-2)+3)-3]/3}-3)"))

if __name__ == "__main__":
    main()