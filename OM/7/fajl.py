#!/usr/bin/env python3

def main():
    f = open("szoveg.txt", "r")

    #for line in f:
     #   line = line.rstrip('\n')
      #  if line.endswith("sor"):
       #     print(line)

    #sorok = [ line.rstrip("\n") for line in f]
    #print(sorok)

    tartalom = f.read().splitlines()
    print(tartalom)

    f.close()

if __name__ == "__main__":
    main()