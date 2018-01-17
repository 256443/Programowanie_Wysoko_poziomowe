#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
#ZADANIE 1:
#pobierz imie i wiek, sprawdz czy jest pełnoletni

# imie =  raw_input()
# wiek = input()
#
# def czyPelnoletni(wiek):
#     if(wiek>18):
#         print "Jestes pełnoletni"
#     else:
#         print "Nie jestes pełnoletni"
#
#
# print "Czesc " + imie +", masz lat " +str(wiek)
# czyPelnoletni(wiek)

#-------------------------------------------------------------------------

#ZADANIE 2
#Pobierz od uzytkownika 3 liczby i wyświetl najwieksza
#
#
# def wys(*dane):
#     for x in dane:
#         print x
#
# def pobierz_liczby(licznik):
#     dane = []
#     for x in range(licznik):
#         zmienna = input('podaj cyfre')
#         dane.append(zmienna)
#     return dane
#
# def znajdzMax(*dane):
#     print "wartosc z tablicy z indexu 0 " +str(dane[0])
#     maxx=dane[0]
#     for x in dane:
#         if(x>maxx):
#             maxx=x
#     print "Max wynois: "+str(maxx)

# licznik = input("ile cyfr?")
# wczytane_dane = pobierz_liczby(licznik)
# wys(*wczytane_dane)
# znajdzMax(*wczytane_dane)
#-------------------------------------------------------------------------

# ZADANIE 3
#wydrukuj na ekranie alfabet w postaci mala litera ->duza litera
# import string
# print "Zadanie 3"
#
# for x in range(26):
#     print string.ascii_lowercase[x],
#     print string.ascii_uppercase[x],

#-------------------------------------------------------------------------
# ZADANIE 4
# Zmodyfikuj poprzedni program tak aby wyswietlał co n-ta litere z alfabetu.Liczbe n wprowadza uzytkownik

# import string
# print "Zadanie 3"
#
# liczba = input("Podaj co która litere mam wyswietlic")
#
# for x in range(26):
#     if(x%liczba==0):
#         print string.ascii_lowercase[x],
#         print string.ascii_uppercase[x],

#-------------------------------------------------------------------------

# ZADANIE 5
#pobierz od uzytkownika N liczb i wyswietl je posortowane. Uzytkownik wybiera kieunek sortowania
# oraz zakres liczb ktore zostana wyswietlone na ekranie


ilosc=input('podaj ilosc cyfr: ')

list = []
print "Wpisz teraz liczby które chcesz posortować"
for i in range(ilosc):
    liczba = input()
    list.append(liczba)

zakres=input('podaj ile wyswietlic posortowanych cyfr (jesli podasz wiecej niz jest wszystkich cyfr, wyswietle wszystkie) :  ')
if(zakres>ilosc):
    zakres=ilosc

kolejnosc = raw_input("wybierz kierunek sortowania: od_lewej lub od_prawej")

try:
    if(kolejnosc=="od_lewej"):
        list.sort()
        licznik=0
        while licznik<zakres:
            print list[licznik]
            licznik+=1
    elif(kolejnosc=="od_prawej"):
        list.sort(reverse=ilosc)
        licznik = 0
        while licznik<zakres:
            print list[licznik]
            licznik+=1
finally:
        print "Bład w wyborze kierunku sortowania"
#
#-------------------------------------------------------------------------


# ZADANIE 6
#wyswietl ciag fibonacciego dla podanej ilosci

# numbers =[0,1]
# n_ty = raw_input("Do ktorego wyrazy mam wyswoetlic")
#
# def fib(numbers):
#     new = 0
#     for i in range(int(n_ty)):
#         new = numbers[-1] + numbers[-2]
#         numbers.append(new)
#         print new
#
#
# fib(numbers)

#-------------------------------------------------------------------------

# ZADANIE 7
# szyfr cezara
# funkcja chr: Na przykład chr(97) zwróci napis 'a'
# funkcja ord dziala odwrotnie do chr
# 122 - jest to w asci = 'z'
# KLUCZ = 3
# def szyfruj(txt):
#     zaszyfrowny = ""
#     for i in range(len(txt)):
#         if ord(txt[i]) > 122 - KLUCZ:
#             zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 21)
#         else:
#             zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
#     return zaszyfrowny
#
#
# tekst = raw_input("Podaj ciąg do zaszyfrowania:\n")
# print szyfruj(tekst)
