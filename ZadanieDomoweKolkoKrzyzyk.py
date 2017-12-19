#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

def createBoard():
    tab = ['#'] * 3
    tabBool = ['$'] * 3
    for x in xrange(len(tabBool)):
        tabBool[x] = ['$'] * 3
        tab[x] = ['#'] * 3
    return tabBool,tab

def printBoard(tab):
    a='A'
    b='B'
    c='C'
    tmp=1
    print ("    %d    %d    %d" % (tmp,tmp+1,tmp+2))
    tmp=0
    for i in tab:
        print string.ascii_uppercase[tmp],i
        tmp+=1

def reductionCharX(a):
    if(a=='A'):
        a=0
        return a
    elif(a=='B'):
        a=1
        return a
    elif(a=='C'):
        a=2
        return a

def reductionCharY(b):
    if(b=='1'):
        b=0
        return b
    elif(b=='2'):
        b=1
        return b
    elif(b=='3'):
        b=2
        return b

def add_X(a,b,tab,tabBool):
    x = reductionCharX(a)
    y = reductionCharY(b)
    tab[x][y] = "X"
    tabBool[x][y] ='X'

def add_O(a,b,tab,tabBool):
    x = reductionCharX(a)
    y = reductionCharY(b)
    tab[x][y]='O'
    tabBool[x][y]='O'

def verificationWinner(tab,znak):
    if(tab[0][0]==znak and tab[0][1]==znak and tab[0][2]==znak):
        print "Zwyciestwo ",znak
        return True
    elif(tab[0][0]==znak and tab[1][1]==znak and tab[2][2]==znak):
        print "Zwyciestwo ",znak
        return True
    elif(tab[0][0]==znak and tab[1][0]==znak and tab[2][0]==znak):
        print "Zwyciestwo ",znak
        return True
    elif(tab[2][0]==znak and tab[2][1]==znak and tab[2][2]==znak):
        print "Zwyciestwo ",znak
        return True
    elif(tab[0][2]==znak and tab[1][2]==znak and tab[2][2]==znak):
        print "Zwyciestwo ",znak
        return True
    elif(tab[0][2]==znak and tab[1][1]==znak and tab[2][0]==znak):
        print "Zwyciestwo ",znak
        return True
    elif(tab[0][1]==znak and tab[1][1]==znak and tab[2][1]==znak):
        print "Zwyciestwo ",znak
        return True
    elif(tab[1][0]==znak and tab[1][1]==znak and tab[1][2]==znak):
        print "Zwyciestwo ",znak
        return True
    else:
        return False

def itsFree(tab,a,b):
    x = reductionCharX(a)
    y = reductionCharY(b)
    if(tab[x][y]=="X" or tab[x][y]=="O" ):
        return True
    else:
        return False

def isCorrectwX(wX):
    if ((wX == "" or (wX != 'A' and wX != 'B' and wX != 'C'))):
        return True
    return False

def isCorrectwY(wY):
    if ((wY == "" or (wY != '1' and wY != '2' and wY != '3'))):
        return True
    return False

def enterTheX():
    wX = raw_input("Podaj wspolrzedna X")
    while (isCorrectwX(wX) == True):
        wX = raw_input("Bledne dane, wprowadz jeszcze raz wpolrzedna X")
    return wX

def enterTheY():
    wY = raw_input("Podaj wspolrzedna Y")
    while (isCorrectwY(wY)):
        wY = raw_input("Bledne dane, wprowadz jeszcze raz wpolrzedna y")
    return wY

def isDraw(symbol):
    if(symbol>9):
        print "Rozgrywka zakonczona remisem"
        return True

def StartGame():
    print 'START'

    tabB,t = createBoard()
    printBoard(t)
    symbol = 1
    while symbol<=9:
        print 'Gracz 1 - X'
        wX = enterTheX()
        wY = enterTheY()
        while (itsFree(tabB, wX, wY) == True):
            print "To pole jest juz zajete, podaj inne wolne pole"
            wX = enterTheX()
            wY = enterTheY()
        add_X(wX,wY,t,tabB)
        printBoard(t)
        if(verificationWinner(t,'X')==True):
            return

        symbol+=1
        while(isDraw(symbol)):
            return

        print 'Gracz 2 -- O'
        wX = enterTheX()
        wY = enterTheY()
        while (itsFree(tabB, wX, wY) == True):
            print "To pole jest juz zajete, podaj inne, wolne pole"
            wX = enterTheX()
            wY = enterTheY()
        add_O(wX,wY,t,tabB)
        printBoard(t)
        if (verificationWinner(t,'O') == True):
            return
        symbol += 1
        while (isDraw(symbol)):
            return

    print "Rozgrywka zakonczona remisem"
    return

StartGame()