# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Zadanie1
#  Napisz funkcję ktora wczytuje plik oraz wczytuje zmienna width w konsoli,
# nastepnie wyswietla tekst tak, ze w jednej lini bedzie nie wiecej niz width znaków

# def wczytaj():
#     width = 0
#     width = input("Podaj liczbe ")
#
#
#     file = open('start_in_git.txt','r').read()
#     lines = file.split('\n')
#     for line in lines:
#         print line[0:width]
#
# wczytaj()

# ------------------------------------------
# Zadanie2
# Zmodyfikuj poprzedni program tak aby wswietlany program był wysrodkowany w obrebie wprowadzonego rozmiaru (width)
# def wczytaj():
#     width = 0
#     width = input("Podaj liczbe ")
#
#
#     file = open('start_in_git.txt','r').read()
#     lines = file.split('\n')
#     for line in lines:
#         print line.strip().center(width)
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
#

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




# Zadanie5 (walidajcja)

# Napisz program który magazynuje informacje o posiadanych ksiązkach(tytul, nr ISBN, autor).
# Program ma miec możliwość dodawania, usuwania, wyswietlania pozycji oraz zapisu stanu programu do pliku,
# jak i możliwosc jego wczytania Sciezke do pliku podajemy w parametrze uruchomieniowym skryptu



























