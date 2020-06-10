# from random import randint  # standart module
# from math import pi, sqrt     # another standart module
# from itertools import count, cycle, repeat
# from itertools import accumulate, takewhile, chain
# from itertools import product, permutations
import random

# print range from 0 to 100 by 5 step or 100 / 5 = 20 items
# print(list(range(0, 100, 5)))

# -------------Docstrings----------------------------------------------------

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


# for i in range(5):
#    value = randint(1,100)
#    print(value)

# --------------------- Exception Handling-------------------------------------

# try:
#    print ( 1 / 0 )
#    print("Done calculation")
# except ZeroDivisionError:
#    print("An error occurred due to zero division") # Result


# try:
#  num1 = input(":")
#  num2 = input(":")
#  print(float(num1)/float(num2))
#
# except:
#  print("Invalid input")

# ____________________________Raising Exceptions________________________________

# print(1)
# raise ValueError
# print(2)

# name = "123"
# raise NameError("Invalid name!")

#num = input(":")
# if float(num)<0:
#    raise ValueError("Negative!")
# else:
#    print("good boy!")

# try:
#     print("some word")
#     num = 5 / 0
# except:
#     print("An error occurred")
#     raise

# __________________________________Assertions______________________________

# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)

# Assertions can be caught and handled like any other exception using the
# try-except statement

# try:
#    temp = -10
#    assert (temp >= 0), "Colder than absolute zero!"
# except:
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

# ------------------------------- .readlines()--------------------------------

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

# ---------------- .write return numbers of bytes written to a file----------------

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


# What is the highest number that would be printed by this code?

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

# Create a list of multiples of 3 from 0 to 20.

# a = [i for i in range(20) if i % 3 == 0]
# print(a)

# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
# print(msg)

# --- String formatting can also be done with named arguments --

# a = "{x}, {y}".format(x=5, y=12)
# print(a)

# ----------- Text Analyzer ---------

# function iterate by character in file text
# def count_char(text, char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count
#
#
# # safely open a file with the specified name
# filename = input("Enter a filename: ")
# with open(filename) as f:
#     text = f.read()
#
# # iterate by alphabet & use func count_char & print Result
# for char in "abcdefghijklmnopqrstuvwxyz":
#     perc = 100 * count_char(text, char) / len(text)
#     print("{0} - {1}%".format(char, round(perc, 2)))


# What is the result of this code?
# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))
# Result: 44

# ==================== Functional Programming =================

# What is the output of this code?
# def test(func, arg):
#   return func(func(arg))
#
# def mult(x):
#   return x * x
#
# print(test(mult, 2))
# Result:  16

# --- pure functions

# def pure_function(x, y):
#     temp = x + 2*y
#     return temp / (2*x + y)
#
#
# print(pure_function(8, 200))

# --- Map (func, arument) --> [list] ----

# def add_five(x):
#     return x + 5
#
# nums = [11, 22, 33, 44, 55]
# result  = list(map(add_five, nums)) # func and list as argument
# print(result) # --------------------- Return new iterable
# # ----------------------------------- with the function
# #                                     applied to each argument

# Map with lambda syntax

# nums = [11, 22, 33, 44, 55]
# 
# result = list(map(lambda x: x + 5, nums))
# print(result) 
# Result [16, 27, 38, 49, 60]

# ----------------------- Filter --------------------

# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res) # Result: [22, 44]

# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1
# 
# for i in countdown():
#     print(i)

# -------------- Generators or Lazy (on demand)-------

# infinite yield --> to stop press Ctrl + с in Windows

# def infinite_sevens():
#     while True:
#         yield 7
# 
# for i in infinite_sevens():
#     print(i)

 
# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
# 
# print(list(numbers(1000)))

# ------------------------ Decorators -----------------

# def decor(func):
#     def wrap():
#         print("=========")
#         func()
#         print("=========")
#     return wrap

# --------- Так неудобно исп. декоратор ------------- 

    # def print_text():
    #     print("Hello world!")

    # decorated = decor(print_text)
    # decorated()

    # def print_text():
    #     print("Hello Lord!")
    # 
    # print_text = decor(print_text)

# -------------- А так гораздо лучше ----------------

# @decor # ---------------- не надо лишний раз объявлять переменные
# def print_text():
#     print("Helllllow my Lord!")
# 
# print_text() # --- Просто вызываем функцию а декоратор уже внутри

# ---------------- Recursion -------------------

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
# 
# print(factorial(5)) # Result: 120

# ------- RecursionError:  maximum recursion depth exceeded

# def factorial(x):
#      return x * factorial(x - 1) 
# 
# factorial(5)

# def is_even(x):
#     if x == 0:
#         return True
#     else:
#         return is_odd(x - 1)
# 
# def is_odd(x):
#     return not is_even(x)
# 
# print(is_odd(17))
# print(is_even(23))

# --------- Fibonacchi --------------

# What is the result of this code?

# def fib(x):
#     if x == 0 or x == 1:
#        return 1
#     else:
#        return fib(x - 1) + fib(x - 2)
# print(fib(4))

# ---------- Sets -------------------

# num_set = {1, 2, 3, 4, 5}
# word_set = set(["spam", "eggs", "sausage"])
# 
# print(3 in num_set) # True
# print("spam" not in word_set) # False
# 
# # Empty Sets or Dictionary 
# 
# empt_set = set() # -- empty Set
# empt_set2 = {} # ---- empty Dictionary
# 
# print(empt_set, empt_set2)


# nums = {1, 2, 1, 3, 1, 4, 5, 6} 
# print("There is a set nums: ", nums) # There is no dupliacate 1 element
# nums.add(-7) # add -7 element
# nums.remove(3) # remove 3 element
# print("There is a changed set nums", nums)
# # Result: {1, 2, 3, 4, 5, 6}
# # {1, 2, 4, 5, 6, -7}

# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}
# print(first | second) # union
# print(first & second) # intersection
# print(first - second) # difference
# print(second - first) # difference
# print(first ^ second) # symmetryc difference


# -------- from itertools import count, cycle, repeat --------------

# for i in count(3):
#     print(i)
#     if i >= 11:
#         break


# -------- from itertools import accumulate, takewhile, chain -----

# nums_accum = list(accumulate(range(8))) # accumulate
# nums2 = list(chain(range(8), nums_accum)) # chain
# 
# print("list range(8)","\n", list(range(8)))
# print("accumulate func","\n", nums_accum)
# # takewhile
# print("takewhile func x<=6","\n", list(takewhile(lambda x: x<=6, nums_accum)))
# print("chain nums2 and nums_accum","\n", nums2)



# nums = [2, 4, 6, 7, 9, 8]
# 
# # ------------ takewhile work while True ------------
# a =  takewhile ( lambda  x: x%2==0, nums)
# print(list(a))
# Result: [2, 4, 6] but not 8


# -------- from itertools import product, permutations ----

# letters = ("A", "B")
# print(list(product(letters, range(4))))
# print(list(permutations(letters)))
# 
# letters_permute = list(permutations(letters))
# print("letters permutable", letters_permute[1])

# ---------------- Module 6 Quiz ---------------

# def power(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y - 1)
# 
# print(power(2, 3))

# Question 3

# a = (lambda x: x * (x + 1))(6)
# print(a)

# Fill in the blanks to leave only even numbers
# in the list

# nums = [1, 2, 8, 3, 7]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)

# Drag and drop from the options below to print 
# only the items in the set "a" that are not in 
# the set "b".

# print (a - b)

# -------- Object-Oriented Programming ----------------

# class Cat:
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs
# felix = Cat("ginger", 4)
# rover = Cat("dog-colored", 4)
# stumpy = Cat("brown", 3)



# class Cat:
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs
# 
# felix = Cat("ginger", 4)
# print(felix.color, felix.legs)

# class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self. color = color
# 
#     def bark(self): # all methods must have self as their first parameter.
#         print("Woof!")
# 
# fido = Dog("Fido", "brown")
# print(fido.name)
# fido.bark()

# class Dog:
#     legs = 4
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# 
# fido = Dog("Fido", "brown")
# print(fido.legs)
# print(Dog.legs)

# undefined attribute

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
# 
# rect = Rectangle(7, 8)
# print(rect.color)

## Result:
## AttributeError: 'Rectangle' object has no attribute 'color'

##  -------------------------  Inheritance ---------------------

# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# 
# class Cat(Animal):
#     def purr(self):
#         print("Purr...")
# 
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
# 
# fido = Dog("Fido", "brown")
# print(fido.color)
# fido.bark()

# class Wolf:# ------------------- Superclass
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# 
#     def bark(self):
#         print("Grr...")
# 
# class Dog(Wolf): # ------------------- Subclass
#     def bark(self):
#         print("Woof")
#     
# husky = Dog("Max", "grey")
# husky.bark()
# 
# ## Result:
# ## Woof

## -------------- indirect inheritance -----------

# class A:
#     def method(self):
#         print("A method")
# 
# class B(A):
#     def another_method(self):
#         print("B method")
# 
# class C(B):
#     def third_method(self):
#         print("C method")
# 
# c = C()
# c.method()
# c.another_method()
# c.third_method()

# Result:
# A method
# B method
# C method

# a = A()
# a.third_method() # --------   AttributeError:

# class A:
#     def spam(self):
#         print(1)
#     
# class B(A):
#     def spam(self):
#         print()
#         super().spam()
# 
# B().spam()
# 
# ## Result:
# # 2
# # 1

# -------- Magic Methods & Operator Overloading -----


# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
# 
# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = first + second
# print(result.x)
# print(result.y)
# 
# ## Result: 
# # 8
# # 16

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
# 
#     def __truediv__(self, other):
#         line = "=" * len(other.cont)
#         return "\n".join([self.cont, line, other.cont])
# 
# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam / hello)

# Result:
# spam
# ============
# Hello world!

# ----------- Magic Methods. Comparisons. ------

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
# 
#     def __gt__(self, other): # gt mean "greater than"
#         for index in range(len(other.cont) + 1):
#             result = other.cont[:index] + " > " + self.cont
#             result += " > " + other.cont[index:]
#             print(result)
# 
# spam = SpecialString("spam")
# eggs = SpecialString("eggs")
# spam > eggs

# ----------- Magic Methods. Others. --------
# Тут мы переназначим ф-ю len() для класса VagueList 
# для возврата случайного числа

# import random
# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont
# # getitem for indexing takes self and index
# # return index + random number form -1 to 1
#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1, 1)]
# 
#     def __len__ (self):
#         return random.randint(0, len(self.cont) * 2)
#     
# vague_list = VagueList(["A", "B", "C", "D", "E"])
# 
# print(len(vague_list)) # переназн. ф-я len() --> random
# print(len(vague_list)) 
# print(vague_list[2]) # 
# print(vague_list[2])

# a = 42  # Create object <42>
# b = a   # Increase ref. count of <42>
# c = [a] # Increase ref. count of <42>
# print(a)
# 
# del a     # Decrease ref. count of <42>
# print(a)
# b = 100   # Decrease ref. count of <42>
# c[0] = -1 # Decrease ref. count of <42>


# class Queue:
#     def __init__(self, contents):
#         self._hiddenlist = list(contents)
# 
#     def push(self, value):
#         self._hiddenlist.insert(0, value)
# 
#     def pop(self):
#         return self._hiddenlist.pop(-1)
# 
#     def __repr__(self):
#         return "Queue({})".format(self._hiddenlist)
# 
# queue = Queue([1,2,3])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue._hiddenlist)


# Double underscore mangled the names

class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)