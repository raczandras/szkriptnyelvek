#!/usr/bin/env python3

SZOVEG ="""A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""



def make_dict():
	ekezetes = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
	csere = "aeiooouuuAEIOOOUUU"
	d = {}
	
	i = 0
	while i < len(ekezetes):
		d[ekezetes[i]] = csere[i]
		i += 1
        
	return d

def main():
    cseretar = make_dict()
    eredmeny = SZOVEG

    for k in cseretar.keys():
        eredmeny = eredmeny.replace(k, cseretar[k])
    
    print(eredmeny)
#############################################################################

if __name__ == '__main__':
    main()
