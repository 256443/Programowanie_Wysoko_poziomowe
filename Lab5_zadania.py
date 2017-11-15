# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Zadanie1
#  Napisz funkcję ktora wczytuje plik oraz wczytuje zmienna width w konsoli,
# nastepnie wyswietla tekst tak, ze w jednej lini bedzie nie wiecej niz width znaków

# def wczytaj():
#     width = input("Podaj liczbe ")
#     plik = open('start_in_git.txt')
#     try:
#         lines = open('start_in_git.txt').read()
#         for lines in len(width):
#             print lines
#         # with open('start_in_git.txt') as fp:
#         #     lines = fp.read().split(len(width))
#
#     finally:
#         plik.close()
#
#     print lines
#
# wczytaj()

# ------------------------------------------
# Zadanie2
# Zmodyfikuj poprzedni program tak aby wswietlany program był wysrodkowany w obrebie wprowadzonego rozmiaru (width)
# def wczytaj():
#     width = input("Podaj liczbe ")
#     plik = open('start_in_git.txt')
#     try:
#         lines = open('start_in_git.txt').read()
#         for lines in len(width):
#             print lines
#         # with open('start_in_git.txt') as fp:
#         #     lines = fp.read().split(len(width))
#
#     finally:
#         plik.close()
#
#     print lines
#
# wczytaj()

# ___________________________________________

# Zadanie 3
# Napisz program który wczytuje plik i wyłuskuje z niego wszystkie poprawne adresy ipV4

import re
# regex_email = re.compile(r'''(?P<adres>(?P<login>[\w+.]+)@(?P<domena>[\w+.\w+]+))''', re.IGNORECASE | re.VERBOSE)
#
# tekst = u'"mail1@poczta.pl", "jan.nowak@wp.eu"'
# for match_string in regex_email.finditer(tekst):
#     print match_string.groupdict()

# regex_ipV4  = re.compile(r'''' (?P<adresIPV4>(?P<w1>[0,1,2]+.+)''''
# plik = open('start_in_git.txt')
# try:
# 	tekst = plik.read()
#
# finally:
# 	plik.close()
#
# print tekst
# -------------------------------------------------------------
# import re
# k = 0
# while k < 5 :
#     i = input("\nEnter Ip address :")
#     ipv4_address = re.compile(
#         '^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
#     k = k + 1
#     if ipv4_address:
#         print ("\n=====================")
#         print ("Valid IP address")
#         print ("=====================")
#         break
#     else :
#         print ("\nInvalid IP")
# else :
#     print ("\nAllowed Max 5 times")

# ----------------------------------------------------------------
#
# import ipaddress
#
# for ip in ["255.255.255.255", "0.0.0.2", "192.168.0.256"]:
#     try:
#         ipaddress.ip_address(ip)
#         print("{} is valid".format(ip));
#     except ValueError:
#         print("{} is invalid".format(ip))
# --------------------------------------------------------------------
# Zadanie4
# Napisz walidator dla numerów pesel, ktory sprawdzi jego poprawność oraz wyłuskuje z niego date urodzenia w postaci dd-'miesiac'-rrrr oraz płec

import re


def sprawdz(pesel):
    # Sprawdzanie regexpem
    if (re.match('[0-9]{11}$', pesel)):
        pass
    else:
        return 0
    # Sprawdzenie sumy kontrolnej...
    l = int(pesel[10])
    suma = (
    (l * int(pesel[0])) + (3 * int(pesel[l])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + ((l * int(pesel[4]))) + (
    3 * int(pesel[5])) + (7 * int(pesel[6])) + (9 * int(pesel[7])) + (l * int(pesel[8])) + (3 * int(pesel[9])))
    kontrolka = 10 - (suma % 10)
    if kontrolka == 10:
        kontrolka = 0
    else:
        kontrolka = kontrolka

    # kontrolka i sprawdzenie zgodnosci
    if ((kontrolka == 10) or (kontrolka == 0)):
        return 0
    else:
        return 1


def index():
    pobranie = raw_input('Podaj PESEL: ')
    p = int(pobranie[9]) % 2
    r = int(pobranie[0:2])
    m = pobranie[2:4]
    d = pobranie[4:6]
    if (sprawdz(pobranie)):
        # sprawdzamy plec
        if p == 1:
            plec = "Mezczyzna"
        else:
            plec = "Kobieta"
        # sprawdzamy rok urodzenia
        if r < 99 and r > 10:
            pr = 1900
        else:
            pr = 2000
        # sprawdzamy miesiac
        if m == '01':
            mies = "Stycznia"
        elif m == '02':
            mies = "Lutego"
        elif m == '03':
            mies = "Marca"
        elif m == '04':
            mies = "Kwietnia"
        elif m == '05':
            mies = "Maja"
        elif m == '06':
            mies = "Czerwca"
        elif m == '07':
            mies = "Lipca"
        elif m == '08':
            mies = "Siperpnia"
        elif m == '09':
            mies = "Wrzesnia"
        elif m == '10':
            mies = "Pazdzierniaka"
        elif m == '11':
            mies = "Listopada"
        elif m == '12':
            mies = "Grudnia"
        else:
            print "Zly PESEL !"
            print "Data urodzenia: %s %s %d %d"
            print "Plec: %s" % plec
    else:
        print "Zly PESEL !"

    print "Twoja data urodzenia to: ", pr + r, m, d
    print "Twoja plec to: ", plec


index()


# Zadanie5 (walidajcja)

# Napisz program który magazynuje informacje o posiadanych ksiązkach(tytul, nr ISBN, autor).
# Program ma miec możliwość dodawania, usuwania, wyswietlania pozycji oraz zapisu stanu programu do pliku,
# jak i możliwosc jego wczytania Sciezke do pliku podajemy w parametrze uruchomieniowym skryptu



























