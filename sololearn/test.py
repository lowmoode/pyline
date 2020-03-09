from random import randint  # standart module
from math import pi, sqrt     # another standart module
 

# print range from 0 to 100 by 5 step or 100 / 5 = 20 items
# print(list(range(0, 100, 5))) 

#-------------Docstrings----------------------------------------------------

#   def shout(word):  
#       """  
#       Print a word with an  
#       exclamation mark following it.  
#       """  
#       print(word + "!")  
# 
# Docstrings retained throughout the runtime of the program

# def printWord(word):
#     print(word)
# 
# neWord = printWord
# neWord("hello") # print hello in terminal


#for i in range(5):
#    value = randint(1,100)
#    print(value)

# --------------------- Exception Handling-------------------------------------

# try:
#    print ( 1 / 0 )
#    print("Done calculation")
# except ZeroDivisionError:
#    print("An error occurred due to zero division") # Result

 

#try:
#  num1 = input(":")
#  num2 = input(":")
#  print(float(num1)/float(num2))
# 
#except:
#  print("Invalid input")

#____________________________Raising Exceptions________________________________

# print(1)
# raise ValueError
# print(2)

# name = "123"
# raise NameError("Invalid name!")

#num = input(":")
#if float(num)<0: 
#    raise ValueError("Negative!")
#else:
#    print("good boy!")

# try:
#     print("some word")
#     num = 5 / 0
# except:
#     print("An error occurred")
#     raise

#__________________________________Assertions______________________________

# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)

# Assertions can be caught and handled like any other exception using the 
# try-except statement

#try:
#    temp = -10
#    assert (temp >= 0), "Colder than absolute zero!"
#except:
#     print ("cold")

# _________________________________Открытие и чтение файла____________________________

file = open("textfile.txt", "r")
cont = file.read()
print(cont)
file.close()