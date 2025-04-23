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
#We know that each SuPrP2 number is in the formula x = p (prime) + 2^k
def allSuPrP2_Nums(n):
    x = n + 1
    while True:
        #Check if x can be written as p + 2^k
        for power in powersOf2Generator():
            if power >= x:
                break
            p = x - power
            if is_prime(p):
                yield x
                break
        x += 1


#Let N be your student ID number (113540137). Use the generator to find 20 consecutive SuPrP2 right after N

def generateFirstTwentySuPrP2(n):
    generator = allSuPrP2_Nums(n)
    list = []
    while len(list) < 20:
        list.append(next(generator))
    return list


#Driver code
n = 113540137
finalList = generateFirstTwentySuPrP2(n)
print(finalList)

#The answer for question 3 will be posted as a comment in the source code - source code will be submitted as a text file
#[113540139, 113540145, 113540147, 113540149, 113540151, 113540153, 113540155, 113540157, 113540161, 113540163, 
# 113540165, 113540167, 113540169, 113540171, 113540173, 113540175, 113540177, 113540179, 113540181, 113540185]