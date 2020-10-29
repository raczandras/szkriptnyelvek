#!/usr/bin/env python3

def main():
    f = open("szoveg.txt", "w")

    print("hello", file=f)
    print("world", file=f)

    f.write("ab\n")
    f.write("ba\n")

    f.close()

if __name__ == "__main__":
    main()