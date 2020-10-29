#!/usr/bin/env python3
INPUT = "string1.py"
OUTPUT = "string1_clean.py"

def main():
    with open(INPUT, "r") as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            if line.strip().startswith("#!"):
                to.write(line)

            elif not line.strip().startswith("#"):
                to.write(line)


if __name__ == "__main__":
    main()