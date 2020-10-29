#!/usr/bin/env python3
INPUT = "string1.py"
OUTPUT = "string1_clean.py"

def main():
    f1 = open(INPUT, "r")
    to = open(OUTPUT, "w")

    for line in f1:
        if line.strip != "#!/usr/bin/env python3":
            print(line)
            if not line.strip().startswith("#"):
                to.write(line)

    f1.close
    to.close

if __name__ == "__main__":
    main()