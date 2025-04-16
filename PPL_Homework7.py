#####   Edward Wages - Homework 7 - Python Yield   #####

#Notes
#You may use functions developed in class, but no modules can be imported
#Efficacy of the program is important
#The answer for question 3 will be posted as a comment in the source code - source code will be submitted as a text file

# We call an integer SuPrP2 if it can be written as a sum of a prime and a power of 2. For example, 
# 15 is a SuPrP2 since 15 = 13 + 21, but 16 is not



#Write a Python generator that yields all powers of two starting from 1 (2^0)
    #ALL powers of 2? That's gonna result in a lot of ridiculous numbers
    #I guess that means we need to loop from 1 to MAX_INT? Is that even an option without importing modules?
    #In a (infinite?) loop, generate all powers of two
    #Naturally, we can do this in a limited loop & append each result into an array, then return that array

#Write a Python generator that on an input (positive integer) n, yields all SuPrP2
#numbers in the increasing order that are greater than n.

#Let N be your student ID number (113540137). Use the generator to find 20 consecutive SuPrP2 right after N