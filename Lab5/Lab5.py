# !/usr/bin/env python
# -*- coding: utf-8 -*-

# # napisUnicode = u"cos tam cos tam"
# # napisStr = napisUnicode.encode('utf8')
# #
# # print isinstance(napisStr,basestring)
#
# # slajd2
# # napisUnicode = u"cos tam cos tam"
# # napisStr = napisUnicode.encode('utf8')
#
# # print isinstance(napisStr,basestring)
# # slajd 3
# napis = u"      test"
# print napis.strip()
# # wysrodkowanie
# print napis.strip().center(30)
#
# # pierwsza litera jest wielka
# print napis.strip().capitalize()
# print napis.strip().lower().islower()
#
# # sprawdzamy czy napisa zaczyna sie od jakiegos tekstu
# print napis.startswith("      t")
#
# # justowanie
# # print napis.ljust()
#
# print napis.swapcase()
# print napis.replace('test', "test")

# Wyrazenia regularne

import re
regex_email = re.compile(r'''(?P<adres>(?P<login>[\w+.]+)@(?P<domena>[\w+.\w+]+))''', re.IGNORECASE | re.VERBOSE)

tekst = u'"mail1@poczta.pl", "jan.nowak@wp.eu"'
for match_string in regex_email.finditer(tekst):
    print match_string.groupdict()




#Serializacja obiektów
#JSON
import json
print 'JSON'.center(50, '-')
import json
slownik = {
    'k1':'w1'
}

jsonStr = json.dumps(slownik)
print jsonStr
print json.loads(jsonStr)

#PICLE
print 'PICLE'.center(50, '-')
import pickle

pickleStr = pickle.dumps(slownik)
print pickle.loads(pickleStr)