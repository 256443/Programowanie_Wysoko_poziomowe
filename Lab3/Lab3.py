#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class Klasa:
#
#     def funkcja(self, zmienna):
#         print "metoda i jej wywolanie %s. " %zmienna
#         self.funkcja2()
#
#     def funkcja2(self):
#         print "funkcjaaaaaa"
#
# obiekt = Klasa()
# obiekt.funkcja("funkcjaaaaaaaaaaaaaaaaaaaaa")


# class klasa22:
#     atr1 = None
#     __atr2 = None
#     def setAtr2(self, zmienna):
#         self.__atr2 = zmienna
#     def setAtr3(self, zmienna):
#         self.__atr3 = zmienna
#
#     def add(self):
#         return self.atr1 + self.__atr2 + self.__atr3
#
# obiekt = klasa22()
# obiekt.atr1 = 4
# obiekt.setAtr2(5)
# obiekt.setAtr3(10)
# obiekt._klasa

# dziedziczenie
# class Samochod:
#     kolor = None
#     def setKolor(self,kolor):
#         self.kolor = kolor
# class osobowy(Samochod):
#     marka = "mercedes"
#
# sam = osobowy()
# sam.setKolor("czerwony")
# print "to jest : %s %s" %(sam.marka, sam.kolor)

# super
# class A:
#     def funkcja(self):
#         print "Wywołanie A"
#
# class B(A):
#     def funkca(self):
#         print "Wywolanie B"
#         super(B, self).funkcja()
#
# B().funkcja()

class A:
    def __init__(self,zmienna):
        self.zmienna = zmienna;
    def __sub__(self, other):
        return self.zmienna - other.zmienna

a= A(5)
b= A(8)
c = A.__sub__(a,b)
print c