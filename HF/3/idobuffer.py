#!/usr/bin/env python3

def main():
    print("tízmillió")
    parts = []
    for i in range(1, 1000000+1):
        parts.append(str(i))
    
    res = "".join(parts)

if __name__ == "__main__":
	main()