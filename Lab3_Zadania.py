#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Zadanie 1:
# ZAimplementuj klase "Liczba zespolona". Klasa ma miec mozliosc dodawania, odejmowania, mnozenia, dzielenia oraz orazz przepisywania
# z wykorzystanie standardowych operatorów. Dodatkow ma miec funkcje "modul" obliczajacą modół liczby zespoloniej oraz mozliwosc porownania go
# przy pomocy sytandardowych operatorów logicznych. Po przekazaniu obiektu do funkcji print ma zostac ona wyswietlona na ekranie

# class LiczbaZespolona:
#     def __init__(self,r,i):
#         self.r = r
#         self.i = i
#     def __add__(self, other):
#         return LiczbaZespolona(self.r+other.r, self.i + other.i)
#     def __sub__(self, other):
#         return LiczbaZespolona(self.r - other.r, self.i - other.i)
#
# a = LiczbaZespolona(2,4) + LiczbaZespolona(7,1)
# b = LiczbaZespolona(2,4) - LiczbaZespolona(7,1)
#
# print "%d + %di" %(a.r, a.i)
# print "%d + %di" %(b.r, b.i)
# -------------------------------------------------
# Zadanie 2:
# Zaimplementuj dwie klasy, punkt 2D i rozszeżającą ja klasę Punkt3D. Kazda klasa ma mieć możliwość obliczania odleglosci miedzy dwoma punktami
# import math
#
# class Punkt2D:
#
#     def __init__(self,a ,b):
#         self.a = a
#         self.b = b
#
#     def fun(punkty, kontrolny):
#         lista_wynikow = []
#         Kx = kontrolny[0].__getitem__(0)
#         Ky = kontrolny[0].__getitem__(1)
#         print "Kx: ", Kx, " Ky: ", Ky
#         for x in range(len(punkty)):
#             Ax = punkty[x].__getitem__(0)
#             Ay = punkty[x].__getitem__(1)
#             print "Obliczam"
#             wynik = math.sqrt(((Kx - Ax) ** 2) + ((Ky - Ay) ** 2))
#             wynik = format("%.2f") % wynik
#             print wynik
#             lista_wynikow.append((Ax, Ay, wynik))
#         return lista_wynikow
#
#
# l = [(2, 5), (3, 2), (5, 9)]
# k = [(5, 9)]
# obiekt = Punkt2D(l,k)
#
# class Punkt3D(Punkt2D):




# ------------------------------------------
# Zadanie 3:
# Zaimplementuj klase samochód posiadajaącą prywatne pola:
# marka
# pojemnosc baku
# predkosc max
# zuzycie paliwa
#
# funkcje publiczne:
# konstruktor
#
# jedz(predkosc,odleglosc) wyswietlacjacą informacje o predkosci (nie wieksza niz max0),czasie podrózy zuzyciu paliwa oraz ile razy trzba bedzie tankowac
# jezeli samochód jedzie ponizej 30% lub powyzej 80% predkosci maxxx to zuzycie wzrasta o 20%
#
# Nastepnie zdefiniuj klasę kabriolet dziedziczac po samochodzie posiadajaca dodatkowe pola :
# otwarty dach
# oraz dwie dodatkowe metody:
# zamknijDach oraz otwórz dach
# Jezeli dach jest otwarty to zuzycie paliwa podaczas obliczen w funkcji jedz powinno wzrosnąc o 15%


