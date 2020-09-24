#!/usr/bin/env python3

def main():
	car_info = [('Suzuki', 'Swift', 1995),
				('Toyota', 'Corolla', 2004),
				('Audi', 'A3', 2008),
				('Seat', 'Cordoba', 2003), 
				('Opel', 'Insignia', 2012), 
				('Mazda', '6', 2018),
				('Mclaren', 'P1', 2015)]

	print("{0:<11} | {1:<11} | {2:<11} |".format("Márka", "Modell","Gyártási év"))
	print("-"*41)

	for car in car_info:
		print("{0:<11} | {1:<11} | {2:^11} |".format(car[0], car[1], car[2]))

if __name__ == '__main__':
	main()