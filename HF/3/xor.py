#!/usr/bin/env python3

def main():
    sztring1 = 0
    sztring2 = "python"

    if bool(sztring1) and not bool(sztring2) or (bool(sztring2) and not bool(sztring1)):
        print("Teljesül a feltétel")
    else:
        print("Nem teljesül a feltétel")


if __name__ == "__main__":
	main()