# Python program to display all the prime numbers within an interval
lower = 0

upper = input("Podaj zakres do ilu liczby mam wypisywac: ")
for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)