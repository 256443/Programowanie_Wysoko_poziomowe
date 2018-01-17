# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Zadanie1
# Dodaj logowanie do pliku do kalulatora wykonywanego na poprzednich zajeciach. Wykotzrsaj różne poziomy logowania.

# Zadanie2
# Przeprowadz debagowanie dowolnego programu napisanego na poprzednich zajeciach.

# -------------------------------------------------------------------------------
# Komendy:
# help (h) - drukuje listę dostępnych poleceń,
# help NAZWA_POLECNIA - drukuje pomoc dla tego polecenia,
# where (w) - pokazuje listę wywołań, strzałką będzie oznaczone miejsce w którym aktualnie się jest,
# list (l) - pokazuje kod źródłowy aktualnie wykonywanego kodu oraz miejsce w którym zatrzymał się debugger,
# down (d) - skok w dół na liście wywołań,
# up (p) - skok w górę na liście wywołań,
# step (s) - wykonanie linii na której zatrzymał się debugger oraz wejście do środka wykonywanego kodu,
# next (n) - wykonanie linii oraz przejście do następnej linii bez wchodzenia do środka wykonywanego kodu,
# continue (c) - kontynuacja wykonywania kodu do następnego zatrzymania (pdb.set_trace())

# -------------------------------------------------------------------------------------------------------------

import pdb
import math
# Komendy pdb


l=[(2,5), (3,2), (5,9)]
k=[(5, 9)]
print l
print k

# def fun(punkty, kontrolny):
#     lista_wynikow=[]
#     Kx = kontrolny[0].__getitem__(0)
#
#     Ky = kontrolny[0].__getitem__(1)
#     print "Kx: ",Kx ," Ky: ",Ky
#     pdb.set_trace()
#     for x in range(len(punkty)):
#         pdb.set_trace()
#         Ax = punkty[x].__getitem__(0)
#         Ay = punkty[x].__getitem__(1)
#         pdb.set_trace()
#         print "Obliczam"
#         wynik = math.sqrt(((Kx-Ax)**2) + ((Ky - Ay)**2))
#         wynik = format("%.2f") % wynik
#         print wynik
#         lista_wynikow.append((Ax,Ay,wynik))
#     pdb.set_trace()
#     return lista_wynikow
#
# a=fun(l,k)
# print "Wyniki: "
# print a

# Zadanie3
# Dodaj testy jednostkowe do poprzedniego zadania tak aby były jak najbardziej poprawne
# + instalacja srodowisk wirtualnego env
import liczby

class Test(object):
    def test_answer_type(self):
        assert isinstance(liczby.num2text(1), basestring)
    def test_zero(self):
        assert liczby.num2text(0) == 'zero'
    def test_zero(self):
        assert liczby.num2text(1) == 'jeden'
    def test_zero(self):
        assert liczby.num2text(2) == 'dwa'