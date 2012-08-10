#Progject Euler - Problem 7
#Zedwarth
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10001st prime number?

#This is an implementation of the Sieve of Eratosthenes.

p = [2, 3, 5]
#p contains the list of found prime numbers
n = 7
#n contains the current number being tested for primality
while len(p) <=10000: #the loop run until the 10001th prime number is found, starting from 0
    if n % 2 == 0 or n % 5 == 0:
        n += 1
    elif all ([n % x != 0 for x in p]):
#test n for primality by trail division with all the currently know prime numbers
        p.append(n) #if n is found to be prime it is added to the list of prime number
        n+=1 #n increase by 1 to test the next number for primality
    else:
        n += 1 #if n isn't prime then n increase by 1 to test the next number for primality
print(p[-1]) #when the targeted prime number is found print it
