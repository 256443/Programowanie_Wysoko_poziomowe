# -*- coding: utf-8 -*-
imie = 'Przemek '
wiek = 24
srednia = 4.5
print imie + str(wiek) +" "+ str(srednia)

tablica = []
tablica.append(1)
tablica.append("ala")
tablica.append(2)
tablica.append(4)
tablica.append(4.2)

print "TABLICA"
for x in tablica:
    print x

tablica2=[1,3,5,"ala ","nie ma ", 4.5]
print "TABLICA2"
for x in tablica2:
    print x

tablica[0]=tablica2[2]
print "TABLICA"
for x in tablica:
    print x

suma = 1 + 2 * 3 / 4.0
print float(suma)
print 11%3

kwadrat = 7 ** 2
szescian = 2 ** 3
print kwadrat
print szescian

z1 = "witaj"
z2 = "świecie"

tablica3 = tablica + tablica *3

print "TABLICA 3 czyli polaczone tablice 1 i 2"
for x in tablica3:
    print x
wiele_witaj = "witaj" *3
print wiele_witaj