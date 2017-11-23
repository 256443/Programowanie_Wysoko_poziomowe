# -----------------
# funkcja lapiaca wyjatki dzielenia przez 0
# def divide(x,y):
#     try:
#         result = x/y
#     except(ZeroDivisionError, TypeError ) as ex:
#         print ex
#     else:
#         print "bra wyjatkow"
#         return result
#     finally:
#         print "koniec funkcji"
#
# print divide(5,0)

# -------------------------------

# nie dziala
class Wyjatek (Exception):
    pass

try:
    raise Wyjatek("wystapil wyjatek")
except:
    Wyjatek()




# --------------------------------
#Wyswietla zrodlo podaje strony
# import urllib2
#
# response = urllib2.urlopen('https://www.python.org/')
# html = response.read()
# print html
# -----------------

#----------------------------
#Parsowanie XML

from xml.dom import minidom

xml = '''<?xml version = "1.0"?>
<mdomtest>
    <el id="1">
        <test>T1</test>
    </el>
    <el id="2">
        <test>T1</test>
    </el>
</mdomtest>
'''
print xml
doc = minidom.parseString(xml)

els = doc.getElementsByTagName("el")
for el in els:
    print "ELEMENTY"
    print str(el)
    sid = el.getAttribute('id')
    test = el.getElementsByTagName("test")[0]
    print ("id: %s. val: %s") % (sid, test.firstChild.data)

# -------------------------------------