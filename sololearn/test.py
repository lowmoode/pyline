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

# file = open("textfile.txt", "r")
# cont = file.read()
# print(cont)
# file.close()

# file = open("filename.txt", "r")
# print(file.read(5))    # +1 байт на пробел
# print(file.read(5))
# print(file.read(3))
# print(file.read())
# file.close()

# file = open("filename.txt", "r")
# #file.read()
# print("Re-reading")
# print(file.read())
# print("Finished")
# file.close()


# Fill in the blanks to open a file, read 
# its content and print its length.

# file = open("filename.txt", "r")
# str = file.read()
# print(len(str))
# file.close()

#------------------------------- .readlines()--------------------------------

# file = open("filename.txt", "r")
# print(file.readlines())
# file.close()

# Output
# ['Some text in txt file on first line\n', 'Another text in text file on second line'] 

# ------------------------iterate through the lines in the file --------------------

# file = open("filename.txt", "r")
# for line in file:
#     print(line)
# 
# file.close()

# print(len(open("filename.txt").readlines()))

# file = open("newfile.txt", "w")#-----------------  The   "w"   mode will create a file
# file.write("This has been written to a file")
# file.close()
# 
# file = open("newfile.txt", "r")
# print(file.read())
# file.close()


# ------------ откроем прочитаем --------------------


# file = open("newfile.txt", "r")
# print("Reading initial contents")
# print(file.read())
# print("Finished")
# file.close()
# 
# file = open("newfile.txt", "w") # Тут файл создастся либо удалится старый -------
# file.write("Some new text")
# file.close()
# 
# file = open("newfile.txt", "r")
# print("Reading new contents")
# print(file.read())
# print("Finished")
# file.close()

#---------------- .write return numbers of bytes written to a file----------------

# msg = "Hello world!"
# file = open("newfile.txt", "w")
# amount_written = file.write(msg)#  ---------------  return: 12 -------------------
# print("lenght of message", len(msg))# ------------  12
# print(file.write(msg) == len(msg)) #  ------------  True
# print(amount_written)
# file.close()

# try:# ------------------------- Попробуй, тут может быть ошибка
#    f = open("filename.txt")
#    print(f.read())
#    print(1 / 0) # --- ERROR ---
# finally:# --------------------- И наконец
#    f.close()# ----------------- Закрой уже файл 

# with open("filename.txt") as f:#---- метод __exit__ уже встроен-----
#    print(f.read())


#What is the highest number that would be printed by this code?

# try:
#   print(1)
#   assert 2 + 2 == 5
# except AssertionError:
#   print(3)
# except:# ----- Не сработает потому что исключения все закончились
#   print(4)

# --------- .get method in Dictionary -----------------

# pairs = {
#    1: "apple",
#    "orange":[2,3,4],
#    True: False,
#    None: "True",
# }
# 
# print(pairs.get("orange"))
# print(pairs.get(7))
# print(pairs.get(12345, "not in dictionary"))

# -------------------------- Tuples -------------------

# tuple = (1, (1,2,3))
# print(tuple[1])

# ---------- Можно указать индекс за пределами списка -----

# list = ["a", "b", "c", "d"]
# a = list[0:5]
# print(a)

# What is the output of this code?

# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(sqs[8:5:-1])
# Result: --------------- [64, 49, 36]

# ----------------------- List Comprehensions ----------------

# cubes = [i**3 for i in range(5)]
# print(cubes)

# -------------- List Comprehensions if statment  ------------


# evens  = [i**2 for i in range(10) if i**2 % 2 ==0]
# evens2 = [i**2 for i in range(10)]
# print(evens2, "\n", evens)

#Create a list of multiples of 3 from 0 to 20.

# a = [i for i in range(20) if i % 3 == 0]
# print(a)

# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
# print(msg)

#--- String formatting can also be done with named arguments --

# a = "{x}, {y}".format(x=5, y=12)
# print(a)



