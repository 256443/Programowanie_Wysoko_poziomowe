#!/usr/bin/env python
# -*- coding: utf-8 -*-
# def suma(a,b):
#     return a+b
#
# imie =  raw_input()
# wiek = raw_input()
# print "Czesc " + imie +" mam lat" +str(wiek)

#Pobierz od uzytkownika 3 liczby i wyświetl najwieksza

# a=input('podaj a: ')
# b=input('podaj b: ')
# c=input('podaj lc: ')
#
# wczytane_dane = (a,b,c)
# print "Wczytane dane to: a=%d, b=%d, c=%d" %wczytane_dane

#wydrukuj na ekranie alfabet w mala litera ->duza litera
import string


# print string.ascii_lowercase + string.ascii_uppercase

# Zmodyfikuj poprzedni program tak aby wyswietlał co n-ta litere z alfabetu.Liczbe n wprowadza uzytkownik

# a=input('podaj liczbe: ')

#pobierz od uzytkownika N liczb i wyswietl je posortowane. Uzytkownik wybiera kieunek sortowania praz zakres liczb ktore zostana wyswietlone na ekranie

# zakres=input('podaj zakres: ')
# ilosc=input('podaj ilosc cyfr: ')
# kolejnosc = raw_input("podaj kolejnosc sortowania")
# list = []
#
# for i in range(ilosc):
#     liczba = input()
#     list.append(liczba)
#
# if(kolejnosc=="od_lewej"):
#     list.sort()
#     for x in list:
#         print x
# elif(kolejnosc=="od_prawej"):
#     list.sort(reverse=ilosc)
#     for x in list:
#         print x
# else:
#     print "Bład w wyborze kolejnosc"

#wyswietl ciag fibonacciego dla podanej ilosci

# numbers =[0,1] #zdefiniuj dwa pierwsze wyrazy ciagu F(0) = 0, F(1) = 1
# n_ty = raw_input("Do ktorego wyrazy mam wyswoetlic")
# print "ile? : "+n_ty
# def fib(numbers):
#     new = 0
#     for i in range(int(n_ty)):
#         new = numbers[-1] + numbers[-2]
#         numbers.append(new)
#         print new
#
# # wywolaj funkcje
# fib(numbers)

# szyfr cezara
# funkcja chr: Na przykład chr(97) zwróci napis 'a'
# funkcja ord dziala odwrotnie do chr
# 122 - jest to w asci = 'z'
KLUCZ = 4
def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 21)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny



tekst = raw_input("Podaj ciąg do zaszyfrowania:\n")
print szyfruj(tekst)
