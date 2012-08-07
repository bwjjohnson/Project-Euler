#Problem-2
#Project Euler
#zedwarth

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a = 1 #a is the newest number in the sequence or F(n)
b = 0 #b is the second newest number in the sequence F(n-1)b
s = 0 #s is the sum of all even numbers

while a < 4000000: #a is check to see if it's less than 4M
    a,b=a+b,a #the next number in the sequence is calculated by adding a+b and giving b the old value of a
    if a%2 == 0: #a is check to be even
        s += a #if it is the vaule is added to the sum
print s #after all the values below 4M have been check the final sum is printed

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
print b
print a
