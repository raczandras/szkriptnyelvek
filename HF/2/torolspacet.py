#!/usr/bin/env python3

def torol(s):
    i = 0
    while i < len(s):
        if s[i] == " ":
            s = s[ : i] + s[i+1 : ]
            i -= 1
        i += 1
    return s

def main():
    ip = "192.168.0.1   :6666"
    print(torol(ip))

if __name__ == "__main__":
	main()