# -*- coding: utf-8 -*-

#tutturuu~
# Tekijä: Camilla Piskonen
# Opiskelijanumero: 0451801
# Päivämäärä: 05.12.2015
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: moniste
import svgwrite

class saatiedot:
	date = 0
	sade = 0
	kalampo = 0
	minlampo = 0
	maxlampo = 0
	

def lataus(nimi):
	
	while True:
		lista = []
		
		try:
			tiedosto = open('%s' % nimi, 'r', encoding='UTF-8')
			for rivi in tiedosto:
				
				tiedot = saatiedot()
				rivi = rivi.split(";")
				tiedot.date = rivi[0]
				tiedot.sade = rivi[1]
				tiedot.kalampo = rivi[2]
				tiedot.minlampo = rivi[3]
				tiedot.maxlampo = rivi[4]
				
				lista.append(tiedot)
				
			del lista[0]
			return lista
			break
		
		except:
			print("Virheellinen syöte.")
			nimi = input("Anna tiedostonimi: ")


def keskiarvo(tiedot1):
	
	s = 0
	p = 0
	for i in tiedot1:
		
		x = float(i.kalampo)
		s = s + x
		p = p+1
		
	ka = round(s/p,1)
	return ka


def minmax(tiedot1):
	
	minlampoja = []
	maxlampoja = []
	for i in tiedot1:
		
		minlampoja.append(float(i.minlampo))
		maxlampoja.append(float(i.maxlampo))
	
	minimi = min(minlampoja)
	maksimi = max(maxlampoja)
	
	arvot = ["",""]
	arvot[0] = minimi
	arvot[1] = maksimi
	
	return arvot
		 
def tallennus(tiedot1):

	while True:
		nimi = input("Anna tiedostonimi: ")
	
		try:
			tiedosto = open('%s' % nimi,'w',encoding='UTF-8')
			
			ka = keskiarvo(tiedot1)
			arvot = minmax(tiedot1)
			minimi = arvot[0]
			maksimi = arvot[1]
		
			plakaatti = ("""Kuukauden säätilasto kaupungissa
*******************************************************
Kuukauden lämpötilan keskiarvo: %s celsiusastetta.
Kuukauden lämpötilan minimi: %s celsiusastetta.
Kuukauden lämpötilan maksimi: %s celsiusastetta.
*******************************************************""" % (ka,minimi,maksimi))
		
			tiedosto.write(plakaatti)
			tiedosto.close
			print("Tallennus onnistui.\n")
			break
		
		except:
			print("Virheellinen syöte.\n")
		

def piirto(tiedot1,nimi):

	lampoja = []
	for i in tiedot1:
		
		lampoja.append(float(i.kalampo))
		
	while True:
		try:
			tiedosto = open('kuvapisteet.csv','w',encoding='UTF-8')
			
			kuva = svgwrite.Drawing('%s' % nimi,size=('600px','600px'))
			pohja = kuva.rect((0,0),(600,600),fill='white')
			kuva.add(pohja)
	
			for i in range(1,6):
			
				i = int(i)
				y = i*100
				viiva = kuva.line((0,y),(600,y),stroke='black',stroke_width='1px')
				kuva.add(viiva)
	
				luku = ((-1*(i*100))/10)+30
				teksti = kuva.text("%s" % luku,((0,(i*100)-3)),style='font-size:20px',fill='green')
				kuva.add(teksti)
			
			for i in range(0,30):
		
				i = int(i)
				x = 20*i
				y = (30-float(lampoja[i-1]))*10
				x2 = 20*(i+1)
				y2 = (30-float(lampoja[i]))*10
		
				v = kuva.line((x,y),(x2,y2),stroke='red',stroke_width='2px')
				pv = kuva.ellipse(center = (x2,y2),r=(1,1),fill='red')
				
				kuva.add(v)
				kuva.add(pv)
				
				if i < 29:	
							
					koordinaatti = str(round(y2))
					suhru = koordinaatti + ","
					tiedosto.write(suhru)
				
				elif i == 29:
					
					koordinaatti = str(round(y2))
					tiedosto.write(koordinaatti)
					
				else:
					tiedosto.close()
				
				
			kuva.save()
			print("Svg- ja csv-tiedostojen kirjoitus onnistui.\n")
			break
		
		except:
			print("Virheellinen syöte.")
			nimi = input("Anna svg-tiedoston nimi: ")




def vertailu(tiedot1):

	nimi = input("Anna vertailtavat säätiedot sisältävän tiedoston nimi: ")
	vtiedot = lataus(nimi)


	vlampoja = []
	for i in vtiedot:
		
		vlampoja.append(float(i.kalampo))
		
	lampoja = []
	for i in tiedot1:
		
		lampoja.append(float(i.kalampo))
		
		
	knimi = input("Anna svg-tiedoston nimi: ")	
	while True:
		try:
			tiedosto = open('kuvapisteet.csv','w',encoding='UTF-8')
			
			
			kuva = svgwrite.Drawing('%s' % knimi,size=('600px','600px'))
			pohja = kuva.rect((0,0),(600,600),fill='white')
			kuva.add(pohja)
	
			for i in range(1,6):
			
				i = int(i)
				y = i*100
				viiva = kuva.line((0,y),(600,y),stroke='black',stroke_width='1px')
				kuva.add(viiva)
	
				luku = ((-1*(i*100))/10)+30
				teksti = kuva.text("%s" % luku,((0,(i*100)-3)),style='font-size:20px',fill='green')
				kuva.add(teksti)
			
			for i in range(0,30):
		
				i = int(i)
				x = 20*i
				y = (30-float(lampoja[i-1]))*10
				x2 = 20*(i+1)
				y2 = (30-float(lampoja[i]))*10
				
		
				v = kuva.line((x,y),(x2,y2),stroke='red',stroke_width='2px')
				pv = kuva.ellipse(center = (x2,y2),r=(1,1),fill='red')
				
				kuva.add(v)
				kuva.add(pv)
				
				if i < 29:	
							
					koordinaatti = str(round(y2))
					suhru = koordinaatti + ","
					tiedosto.write(suhru)
				
				elif i == 29:
					
					koordinaatti = str(round(y2))
					tiedosto.write(koordinaatti)
					
				else:
					tiedosto.write("\n")
				
				
			for i in range(0,30):
			
				vx = 20*i
				vy = (30-float(vlampoja[i-1]))*10
				vx2 = 20*(i+1)
				vy2 = (30-float(vlampoja[i]))*10
				
				w = kuva.line((vx,vy),(vx2,vy2),stroke='blue',stroke_width='2px')
				pw = kuva.ellipse(center = (vx2,vy2),r=(1,1),fill='blue')				

				kuva.add(w)
				kuva.add(pw)
				
				
				if i < 29:	
							
					koordinaatti2 = str(round(vy2))
					suhru2 = koordinaatti2 + ","
					tiedosto.write(suhru2)
				
				elif i == 29:
					
					koordinaatti2 = str(round(vy2))
					tiedosto.write(koordinaatti2)
					
				else:
					tiedosto.close()
	
			kuva.save()
			print("Svg- ja csv-tiedostojen kirjoitus onnistui.\n")
			break
		
		except:
			print("Virheellinen syöte.\n")
			knimi = input("Anna svg-tiedoston nimi: ")


def valikko():

	print("""Säätietojen käsittely
*******************************************************
1) Lataa kaupungin säätiedot tiedostosta
2) Laske keskiarvo kuukauden lämpötiloista
3) Laske kuukauden lämpötilojen minimi ja maksimi
4) Tallenna kuukauden tiedot tiedostoon
5) Piirrä graafi kuukauden lämpötiloista kaupungissa
6) Lataa toiset säätiedot ja piirrä vertailugraafi
0) Lopeta""")

	while True:
		try:
			valinta = int(input("Valintasi: "))
			return valinta
		except:
			print("Virheellinen valinta.")
		
	
	
def paa():
	
	while True:
		try:
			valinta = valikko()
		
			if valinta == 1:
				nimi = input("Anna tiedostonimi: ")	
				tiedot1 = lataus(nimi)
				print("Tiedoston luku onnistui.")
		
			elif valinta == 2:
				ka = keskiarvo(tiedot1)
				print("Kuukauden lämpötilan keskiarvo: %s\n" % ka)
			
			elif valinta == 3:
				arvot = minmax(tiedot1)
				print("""Kuukauden lämpötilan minimi: %s
Kuukauden lämpötilan maksimi: %s\n\n""" % (arvot[0],arvot[1]))
		
			elif valinta == 4:
				tallennus(tiedot1)
			
			elif valinta == 5:
				nimi = input("Anna svg-tiedoston nimi: ")
				piirto(tiedot1,nimi)
		
			elif valinta == 6:	
				vertailu(tiedot1)
			
			elif valinta == 0:
				print("Kiitos ohjelman käytöstä!\n")
				break
  		
			else:
				print("Virheellinen valinta.\n")
				
		except:
			print("Virheellinen syöte. Tarkista onko kaupungin tiedot ladattu.\n")
  		
paa()

#loppu~
