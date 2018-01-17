# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import subprocess
import os
# out1 = subprocess.call(
#     ["ls"], shell=True)
# print (out1)
#
# out2 = subprocess.check_output(
#     ["ls"], shell = True)
#
# print (out2)

# with open(os.devnull, 'w') as devnull:
#     out1 = subprocess.call(
#         ["ls"], stdout= devnull, shell=True)
# out2 = ""
# try:
#     out2 = subprocess.check_call()(
#         ["ls"], stdout= devnull, shell=True)
#
# except subprocess.CalledProcessError as ex:
#     print (ex)
# print (out1)
# print (out2)

# Zadanie 1
# Napisz program który kompiluje kod c++, a nastepnie uruchamia go i sprawdza czy jego wywolanie nie konczy sie błedem


# import subprocess
# out2 = subprocess.call(
#     'g++ -o powtorzenie main.cpp', shell=True)
#
# print (out2)

# Zadanie2
# KOrzystajac z modułu subprocess napisz program który twozrzys strukture katalogów podana w formie:
#
# K1---
#     |K2
#     |K3
#         K4
# K5---
#     K6
import os
# dirStr = '''
# K1
#     K2
#     K3
#         K4
# K5
#     K6'''
# import subprocess
# # for i in dirStr.splitlines():
# #     i=subprocess.Popen("mkdir ", i.strip(), shell=True)
# # # os.chdir("Programowanie_Wysoko_poziomowe\K1")
# p=subprocess.Popen("mkdir K1", shell=True)

# Zadanie3
# http://users.uj.edu.pl/~ufkapano/algorytmy/lekcja09/slist1.html
# Napisz program posiadajacy funkcje krora oblicza rozklad liczby podanej w argumencie na czynniki piwerwsze
# i zwraca wynik w postaci pra krotek [ (p1,w1), (p2,w2)...] takich, ze n = p1 do w1 * p2 do w2.
# Przykład:
# rozklad(756)
# [(2,2), (3,3), (7,1)]

# from math import *
#
#
# def rozklad(x):
#     if x <= 0:
#         return 0
#     i = 2
#     e = floor(sqrt(x))
#     r = []  # używana jest tablica (lista), nie bepośrednie wypisywanie
#     while i <= e:
#         if x % i == 0:
#             r.append(i)
#             x /= i
#             e = floor(sqrt(x))
#         else:
#             i += 1
#     if x > 1: r.append(x)
#         # append(x)
#     return r
#
# print("Podaj liczbę: ")
# l = int(input())
# r = rozklad(l)
# print r

# Zadanie4
# Napisz klase, implementacje własnej obiektowej listy. Program powinien posiadac operacje takie jak dodawanie, usuwanie, sortowanie,
# posiadac przecizaone operatory i zglaszac niezbedne wyjatki.

class myImplementation:

    def add(self,x):
        print ("Dodawanie do listy" + x)


a =myImplementation
a.add(8)