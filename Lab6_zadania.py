#!/usr/bin/env python
# -*- coding: utf-8 -*-
# michal.panczyk.info
# https://tutorial.djangogirls.org/pl/django_installation/

# liczby ujemne
# stringi
# zmienna której nie ma
# Zadanie1
# import math
# try:
#     liczba = input('Podaj cyfre')
#     print float(math.sqrt(liczba))
# except:
#     print "błedne dane"

# zadanie 2
# Napisz klase, która bedzie przechowywac adres email.
# konstruktor ma przjmowac napis, bedacy adresem.
# Jesli zostanie podany niewłasciwy adres, konstruktor ma zglaszac wyjatek odpowiedniej klasy\
#     Walidacja adresu email byc realizownna przy pomocy wyrazen regularnych

# do poprawy

# import re
# regex_email = re.compile(r'''(?P<adres>(?P<login>[\w+.]+)@(?P<domena>[\w+.\w+]+))''', re.IGNORECASE | re.VERBOSE)
# #
# # tekst = u'"mail1@poczta.pl", "jan.nowak@wp.eu"'
# # for match_string in regex_email.finditer(tekst):
# #     print match_string.groupdict()
#
# class EMAIL:
#     def __init__(self, adres):
#         self.adres = adres
#
#
# em = EMAIL("przemek.antoszek")
# # print regex_email.flags(em.adres)
#
# for match_string in regex_email.finditer(em.adres):
#     print match_string.groupdict()

# ---------------------------------------------------

# Zadanie3

# Utwórz za pomoca virtualenv wlasne srodowisko. Doinstaluj do niego pakiet pep8 i sprawdz zgodnosc wlasnych skryptów ze standardem pep8.
# virtualenv envp8
# source/envp8/bin/activate
# pip install pep8


# Zadanie 4
# Napisz program który pobiera dokment html i zapisuje go na dysku

import urllib2

response = urllib2.urlopen('https://www.python.org/')
html = response.read()
plik = open('zrodlo strony', 'w')
plik.write(html)
plik.close()

# print html

# Zadanie 5
# Napisz prosty czytnik RSS.Program ma miec mozliwosc zapamietywania ulubionych kanałów. Wiadomości powinny byc czytelnie sformatowane

# from xml.dom import minidom
#
# xml = open('plik').read()
# # print xml
# doc = minidom.parseString(xml)
#
# els = doc.getElementsByTagName("channel")
# for el in els:
#     # print "ELEMENT"
#     # print el
#     # sid = el.getAttribute('pubDate')
#     test = el.getElementsByTagName("pubDate")[0]
#     print ("pubDate: %s") % (test.firstChild.data)
