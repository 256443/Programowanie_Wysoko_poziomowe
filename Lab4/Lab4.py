#! /usr/bin/env python
# -*- coding: utf-8 -*-
# d = {"k1":"w1", "k2":"w2", "k3" : "w3"}
# print d
#
#
# def wczytaj():
#     d={}
#     x=input("Podaj klucz")
#     y=input("Podaj wartosc")
#     d= {x:y}
#     print d
#
# wczytaj()

# napis = '''k1:w1
# k2:w2
# k3:w3'''
# slownik={}
#
# for line in napis.split('\n'):
#     elementy = line.split(' : ')
#     slownik[elementy[0]] = elementy[1]
#
# print slownik.items()

# zadanie 2
# Zmodyfikuj poprzedni program tak aby identycznie zdefioniowany napis był wczytywany z pliku. Nazwa pliku jest podana w parametrze

# text = open('slownik.txt')
# print text
# text.close()


# Zadanie3

# Napisz program, który w parametrze przyjmuje nazwe pliku. Program ma stworzyc slownik w którym zostanie zliczona ilosc
# wystapien danego slowa we wczytanym tekscie.

#---------
# # Program liczy wszystkie slowa i znaki
# znaki= raw_input().split()
#
# liczby = 0
# slowa = 0
# for i in range(len(znaki)):
#     if znaki[i].isdigit() == 1: liczby += 1
#     else:
#         slowa += 1
#
# print liczby,  slowa

#----------------------

# znaki = list()
# while 1:
#    try:
#       # ^D ^Z
#       znaki.append(raw_input())
#    except EOFError:
#       break
#
# liczby = 0
# slowa = 0
# for linia in znaki:
#    linia = linia.split()
#    for slowo in linia:
#       if slowo.isdigit():
#          liczby += 1
#       else:
#          slowa += 1
#
# print liczby,  slowa


# Zadanie 4

# Napisz program który w parametrze otrzymuje nazwe pliku lub znak "-" oraz ciag znaków.
# Program ma wczytac plik i wyświetlic te linie w których znajduje sie podany ciag znaków.
# Jezeli zamiast nazwy pliku jest znak "-" to linie sa wczytywane ze standardowego wyjscia.
# Pusta linia konczy wczytywanie
#----------------------
# text = open('slownik.txt',"r")
# for line in text:
#     print line

# zmienna = "ala ma kota"
#
#
# text = open('slownik.txt')
# for line in text('\n'):
#     print text.read()
# if text == text.readline():
#     print "is ok" + text
# else:
#     print "wystepuja inne znaki"

# text.close()

# Zadanie 5.
# Napisz program który w parametrze otrzymuje dwie nazwy plików.
# Program ma wczytac jeden plik, zaszyfrowac go szyfrem cezara
# i zapisac pod nowa nazwa z parametru.

text = open('slownik.txt',"r")
file2 = open("nowy.txt", "w")
for line in text:
    print line
    file2.writelines(line)

# for line in file2:
#     print file2.readlines()



text.close()
file2.close()



