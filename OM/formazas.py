#!/usr/bin/env python3

PI = 3.14159

def hello(name, color, what):
	#print("{0}, {1} az {2}!".format(name, color, what))
	
	#print("{}, {} az {}!".format(name, color, what))
	
	print("{nev}, {szin} az {obj}!".format(nev=name.capitalize(),
	 szin=color, obj=what))
	
	#print(f"{name}, {color} az {what}!")
	#print(f"1 + 1 = { 1 + 1 }")
	
def main():
	hello("géza", "kék", "ég")
	print("-" * 30)
	hello("julcsi", "piros", "auto")
	print("-" * 30)
	print(f"pi értéke: {PI}")

if __name__ == "__main__":
	main()
