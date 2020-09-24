#!/usr/bin/env python3

def main():
    
    lista = []
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            lista.append(i)

    print(sum(lista))

if __name__ == "__main__":
	main()