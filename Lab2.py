# Zadanie 1
# korzystajac z list skladanych npisz funkcje która przyjmuje napisa i zwraca liste krotek w postaci (slowo, dlugosc slowa)
# napis = 'Odwazny '
# slowa = napis.split()
# dlugosc_slow = [len(slowo) for slowo in slowa if slowo != 'nad']
#
# print (slowa + dlugosc_slow)


# def pobierz_napis():
#     napis = input("Podaj napis: ")
#     krotka = (napis, len(napis))
#     print("%s, %d" %krotka)
#
# pobierz_napis()

# Zadanie 2
# Korzystajac z list skladanych napisz funkcje króra stworzy liste n elementów ciagu fibonacciego. Liczba n podawana jest w konsoli

#wyswietl ciag fibonacciego dla podanej ilosci


# numbers =[0,1]
# n_ty = input("Do ktorego wyrazy mam wyswoetlic")
#
# def fib(numbers):
#     new = 0
#     for i in range(int(n_ty)):
#         new = numbers[-1] + numbers[-2]
#         numbers.append(new)
#         print (new)
#
#
# fib(numbers)

# Zadanie 3
# Napisz generator do obliczenia ciagów fibonaacciego


# def fib():
#
#     p=0
#     n=1
#     yield p
#     yield n
#
#     while True:
#         t = p+n
#         p=n
#         n=t
#         yield n
#
#
# f=fib()
# print (f.__next__)
# print (f.__next__)

# Zadanie 4
# zaimplementuj funkcje która w argumencie otrzymuje funkcje logiczna oraz liste i zwraca liste elementów spełniajacych warunek podany w przekazanej funkcji

# def pierwsze(n):
#     return [i for i in range(2, n) if len([t for t in range(1, i+1)
#                                            if i % t == 0]) == 2]
#
# ret =pierwsze(10)
# print(ret)
# ----------------

def flog(a):
    return a%3

def ftest (f,l):
    # return f(l)
    return [i for i in range(0,l+1) if f(i)]

print(ftest(flog,4))
print(ftest(flog,10))
# ----------------
# def logiczna(napis):
#     if(len(napis)>5):
#         return True
#     return False

# def fun(fun, *lista):
#     napis = lis
# -------------------------



# Zadanie 5
# zimplementuj funkcje która przyjmuje liste punktów na płaszczyznie w postaci krotek oraz punkt kontrolny
# Funkcja ma zwrocic liste krotek w postaci (odlegolosc, punkty (x,y)) w kolejnosci od najblizszego do najdalszego  pomiedzy elementami z listy a punktem kontrolnym
# ---------------


# Zadanie 6
# Napisz generator który bedzie zwracał nazwy kolejnych plików z katalogu o podanycm rozszezeniu. rozszezenie oraz sciezke podaje zytkownik z konsoli
# wykorzystac listdir(path)




# Generator
# def generator(n):
#     while n:
#         print("Generator start %d" %n)
#         yield n
#         print("Generator stop %d" %n)
#         n-=1
#
#
# for x in generator(5):
#     print("wywolanie %d" %x)


# def podziel(str):
#     return [(slowo, len(slowo)) for slowo in str.split]

# def f1(a):
#     def f2(b):
#         return a - b
#     return f2
#
# res = f1(5)
#
# print (res(10))

# Lambda
# kwadrat = lambda x: x*x
# print(kwadrat(2))

