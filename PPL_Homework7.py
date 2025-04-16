#####   Edward Wages - Homework 7 - Python Yield   #####

#Notes
#You may use functions developed in class, but no modules can be imported
#Efficacy of the program is important
#The answer for question 3 will be posted as a comment in the source code - source code will be submitted as a text file

# We call an integer SuPrP2 if it can be written as a sum of a prime and a power of 2. For example, 
# 15 is a SuPrP2 since 15 = 13 + 21, but 16 is not

#Helper Methods
# is_prime(n) was developed in class on 4/15/2025. It takes a number & checks if it is prime by computing the square of all values before n.
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


#Write a Python generator that yields all powers of two starting from 1 (2^0) (DONE)
def powersOf2Generator():
    i = 1 #initial value of 1 / 2^0
    while True:     #Provides allows us to infinitely acquire the next power 
        yield 2 ** i 
        i += 1

#Write a Python generator that on an input (positive integer) n, yields all SuPrP2
#numbers in the increasing order that are greater than n.
def allSuPrP2_Nums(n):
    #Needs a while True
    #NEeds the rest of the function lmao

#Let N be your student ID number (113540137). Use the generator to find 20 consecutive SuPrP2 right after N