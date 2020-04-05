
# Python

---

## Range

**range()** --> range object создает список чисел  
**list(range(5))** --> [0,1,2,3,4]  
**list(range(3,6))** --> [3,4,5]  
range(20) == range(0,20)  
list(**range(5,20,2)**) --> [5,7,9,11,13,15,17,19]  
Третий аргумент обозначает интервал последовательности  

## Loops  

**while** True - оператор цикла будет исполнять действие  

## for loop  

**for** x **in** someList --> Итерация через список  
**for** i **in range(5)** --> Итерация по заданному списку  

## Задание. Простой калькулятор  

## Functions  

**func_name(func_argument)** аргументы функции  

```python
    def my_func(): -- *define before they are called*
        print("spam")  
```

## Arguments  

* Function arguments cannot be referenced outside of the function's  definition.

## Functions & Modules

---

**\# comment text** - comment block  
**Docstirngs** documentation strings retained  
throughout the runtime of the program

```python
    def shout(word):  
        """  
        Print a word with an  
        exclamation mark following it.  
        """  
        print(word + "!")  
    shout("spam")  
```

Functions can be assigned and **reassigned** to **variables**, and later referenced by those names.  

### Function as arguments  

Functions can also be used as arguments of other functions.

```python
    def add(x, y):
      return x + y
    def do_twice(func, x, y):
      return func(func(x, y), func(x, y))
    a = 5
    b = 10
    print(do_twice(add, a, b)) # print 30 in terminal
```

## Modules

**import** *module_name* at top of your code  
**module_name** *.var* to access functions and value with the name **var**  
 **from math import \*** или импорт всего модуля совсем не рекомендуется  

### Import under a different name

use **as** keyword

```py
    import math import sqrt as square_root
    print(square_root(100)) # print 10.0
```

### The standart Library & PIp

There are three type Modules in Python:  

1. Those ou write yourself
2. Those you install from external sources
3. Those that are preinstalled with Python (standart library)

## Exceptions & Files

Exceptions(исключения) like **ZerDivizionError** when (some_int / 0)  
Common Exceptions:

1. ImportError: an import fails;
2. IndexError: a list is indexed with an out-of-range number;
3. NameError: an unknown variable is used;
4. SyntaxError: the code can't be parsed properly;
5. TypeError: a function is called on a value of an inappropriate type;
6. ValueError: a function is called on a value of the correct type, but with an inappropriate value.

### Exception Handling

**try/except** statment

```py
try:
   print ( 1 / 0 )
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")
```

If no error occurs, the code in the except block doesn't run.  

A try statement can have multiple different except blocks to handle different exceptions  

```py
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError: #------ There
   print("Divided by zero")
except (ValueError, TypeError): # And There
   print("Error occurred") # Result
```

An except statement without any exception specified will catch all errors

```py
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred") # Result
```

### finally  

To ensure some code runs no matter what errors occur, you can use a finally statement.

```py
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")
```

Result:  

```py
Hello
Divided by zero  
This code will run no matter what  
```

### Raising Exceptions

---

You can raise exceptions by using the raise statement.

```py
print(1)
raise ValueError
print(2)
```

Result:  

```py
1
ValueError
```

**Exceptions** can be **raised** with arguments that give detail about them.  
For example:

```py
name = "123"
raise NameError("Invalid name!")
```

Result:

```py
NameError: Invalid name!
```

In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
For example:  

```py
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise
```

Result:

```py
An error occurred
ZeroDivisionError: division by zero
```

### Assertions (Оператор контроля)

An expression is tested, and if the result comes up **false**, an exception is **raised**.  

```py
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
```

Result:

```py
1
2
AssertionError
```

AssertionError exceptions can be caught and handled like any other exception using the **try-except** statement, but **if not handled**, this type of exception will **terminate** the program.

## Opening Files

```py
myfili = open("filename.txt")
```

The argument of the open function is the path to the file. If the file is in the current working directory of the program, you can specify only its name.

You can specify the mode used to open a file:  

* Sending "r" means open in read mode, **which is the default**.
* Sending "w" means write mode, for rewriting the contents of a file.
* Sending "a" means append mode, for adding new content to the end of the file.
* Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files

```py
open("filename.txt", "w")
open("filename.txt", "r")
open("filename.txt", "wb")
```

You can use the + sign with each of the modes above to give them extra access to files. For example, r+ opens the file for both reading and writing.  

Once a file has been opened and used, **you should close it**.
This is done with the close method of the file object.

```py
file.close()
```

## Reading Files

Не забудь переключить терминал в **рабочую директорию** чтобы работать с фалами.  

The contents of a file that has been opened in  
text mode can be read using the read method.  

```py
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()
```

To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file.

```py
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()
```

*Just like passing no arguments, negative values will return the entire contents.*

After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.  

```py
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()
```

To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.

**For example:**

```py
file = open("filename.txt", "r")
print(file.readlines())
file.close()
```

You can also use a **for** loop to iterate through the lines in the file:

```py
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()
```

*In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the end of its output.*

## Writing Files

To write to files you use the write method, which writes a string to the file.  
**For example:**

```py
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()
```

Программа создаст новый файл newfile.txt и запишет в него текст в аргументе.  
При повторном запуске программа опять создаст новый файл и т.д.

*The "w" mode will create a file, if it does not already exist.*

### When a file is opened in write mode, the file's **existing content is deleted**

```py
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()
```

### The write method returns the number of bytes written to a file, if successful  

```py
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
```

**Result:**  

```py
12
```

*To write something other than a string, it needs to be converted to a string first.*  

## Working With Files  

It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally.

```py
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()
```

*This ensures that the file is always closed, even if an error occurs.*

An alternative way of doing this is using with statements. This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.

```py
with open ("filename.txt")as f:
   print(f.read())
```

*The file is automatically closed at the end of the with statement, even if exceptions occur within it.*

## More Types

* None
* Dictionaries
* Tuples
* List Slices
* List Comprehensions
* String Formatting
* Useful Functions
* Text Analyzer

### None

The None object is used to represent the absence of value.  
It is similar to **null** in other programming languages.  
Like other "empty" values, such as 0, [] and the empty string, it is  
**False** when converted to a Boolean variable.  
When entered at the Python console, it is displayed as the empty strin.

```py
>>> None == None
True
>>> None
>>> print(None)
None
>>>
```

The **None** object is returned by any function that doesn't explicitly  
return anything else.

```py
def some_func():
   print("Hi")

var = some_func()
print(var)
```

**Result:**

```py
Hi
None
```

### Dictionaries

**Dictionaries** are data structures used to map arbitraty keys to values.  
List can be thought of as dictionaries with integer keys within a certain range.  
Dictionaries can by indexed in the same way as lists, using **square brakets** containing keys.
**Example:**

```py
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
```

**Result:**

```py
24
42
```

*Each element in a dictionary is represented by a **key:value** pair*

Trying to index a key that isn't part of the dictionary returns a **KeyError**.  
**Example:**

```py
primary = {
   "red":[255,0,0]
   "green":[0,255,0]
   "blue":[0,0,255]
}

print(primary["red"])
print(primary["yellow"])
```

**Result:**

```py
[255,0,0]

KeyError.'yellow'
```

As you can see, a dictionary can store any types of data as values.
*An empty dictionary is defined as {}.*

Only **immutable** objects can be used as keys to dictionaries. Immutable objects are those that can't be changed. So far, the only mutable objects you've come across are **lists** and **dictionaries.**  
Trying to use a mutable objects as a dictionary ky causes a **TypeError.**

```py
bad_dict = {
   [1,2,3]: "one two three",
}
```

**Result:**

```py
TypeError: unhasable type: 'list'
```

Just like lists, dictionary keys can be assigned to different values.
However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.

```py
squares = {1:1, 2:4, 3:"error", 4:16}
squares[8] = 64
squares[3] = 9
print(squares)
```

**Result:**

```py
{1:1, 2:4, 3:9, 4:16, 8:64}
```

To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.  
**Example:**

```py
nums = {
   1:"one",
   2:"two",
   3:"three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
```

**Result:**

```py
True
False
True
```

#### Dictionary .get

A useful dictionary method is **get**. It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead ('None', by default).  
**Example:**

```py
parirs = {
   1: "apple",
   "orange":[2,3,4],
   True: False,
   None: "True",
}

print(paris.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
```

**Result:**

```bash
>>>
[2,3,4]
None # --------------- By Default Value None
not in dictionary
>>>
```

## Tuples

Tuples are very similar to lists, except that they are immutable (they cannot be changed).  
Also, they are created using parentheses, rather than square brackets.  
**Example:**

```py
words = ("spam", "eggs", "sausages",)
```

You can access the value in the tuple with their index, just as you did with lists:

```py
print(words[0])
```

Trying to reassign a value in a tuple causes a TypeError.

```py
word[1] = "cheese"
```

```bash
>>>
TypeError. 'tuple' object does not support item assignment
>>>
```

*Like lists and dictionaries, tuples can be nested within each other.*
Tuples can be created without the parentheses, by just separating the values with commas.  
**Example:**

```py
my_tuple = "one", "two", "three"
print(my_tuple[0])
```

**Result:**

```bash
>>>
one
>>>
```

An empty tuple is created using an empty parenthesis pair.

```py
tpl = ()
```

*Tuples are faster than lists, but they cannot be changed.*

## List slices

List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. This returns a new list containing all the values in the old list between the indices.  
**Example:**

```py
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
```

**Result:**

```bash
[4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]
```

*Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.*  

If the first number in a slice is omitted, it is taken to be the start of the list.
If the second number is omitted, it is taken to be the end.  
**Example:**

```py
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])
```

**Result:**

```bash
[0, 1, 4, 9, 16, 25, 36]
[49, 64, 81]
```

*Slicing can also be done on tuples.*

List slices can also have a third number, representing the step, to include only alternate values in the slice.

```py
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2]) # Every second value on list
print(squares[2:8:3]) # Every third value from 2 to 8 index
```

**Result:**

```bash
[0, 4, 16, 36, 64]
[4, 25]
```

*[2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3.*

Negative values can be used in list slicing (and normal list indexing). When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list.

```py
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])
```

**Result:**

```bash
[1, 4, 9, 16, 25, 36, 49, 64]
```

*If a negative value is used for the step, the slice is done backwards.
Using [::-1] as a slice is a common and idiomatic way to reverse a list.*

## List Comprehensions

List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
For example, we can do the following:

```py
# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)
```

**Result:**

```py
[0, 1, 8, 27, 64]
```

*List comprehensions are inspired by set-builder notation in mathematics.*

Question:  
What does this list comprehension create?
nums = [i*2 for i in range(10)]

Answer:
A list between 0 and 18.  

A list comprehension can also contain an if statement to enforce a condition on values in the list.  
**Example:**

```py
evens = [i**2 for i in range(10) if i**2 % 2 ==0]
print(evens)
```

**Result:**

```bash
[0, 4, 16, 36, 64]
```

Trying to create a list in a very extensive range will result in a **MemoryError**.
This code shows an example where the list comprehension runs out of memory.

```py
even = [2*i for i in range(10**100)]

# Result:

>>>
MemoryError
>>>
```

*This issue is solved by generators, which are covered in the next module.*  

## String Formatting

So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
String formatting provides a more powerful way to embed non-strings within strings. String formatting uses a string's format method to substitute a number of arguments in the string.  
**Example:**

```py
# strin formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)

#Result
>>>
Numbers: 4 5 6
>>>
```

*Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.*  

String formatting can also be done with named arguments.  
**Example:**

```py
a = "{x}, {y}".format(x=5, y=12)
print(a)

# Result:
>>>
5, 12
>>>
```

## Useful Functions

Python contains many useful built-in functions and methods to accomplish common tasks.  

### String Functions

**join** - joins a list of strings with another string as a separator.  
**replace** - replaces one substring in a string with another.  
**startswith** and **endswith** - determine if there is a substring at the start and end of a string, respectively.  
To change the case of a string, you can use **lower** and **upper**.  
The method **split** is the opposite of join, turning a string with a certain separator into a list.  
**Some examples:**

```py
print(", ".join(["spam", "eggs", "ham"])) # list --> string
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", ")) # string --> list
#prints "['spam', 'eggs', 'ham']"
```

### Numeric Functions

To find the maximum or minimum of some numbers or a list, you can use **max** or **min**.  
To find the distance of a number from zero (its absolute value), use **abs**.  
To round a number to a certain number of decimal places, use **round**.  
To find the total of a list, use **sum**.  
**Some examples:**  

```py
print(min(1, 2, 3, 4, 0, 2, 1))
# prints: "0"
print(max([1, 4, 9, 2, 5, 6, 8]))
# prints: "9"
print(abs(-99))
# prints: "99"
print(abs(42))
# prints: "42"
print(sum([1, 2, 3, 4, 5]))
# prints: "15"
```

### List Functions

Often used in conditional statements, **all** and any **take** a list as an argument, and return **True** if all or any (respectively) of their arguments evaluate to **True** (and **False** otherwise).  
The function **enumerate** can be used to iterate through the values and indices of a list simultaneously.  
**Example:**

```py
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)

# Result:

>>>
All larger than 5
At least one is even
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
>>>
```

## Text Analyzer

This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
This section shows how a file could be open and read.

```py
filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()
print(text)
```

This part of the program shows a function that counts how many times a character occurs in a string.

```py
def count_char(text, char):
   count = 0
   for c in text:
      if c == char:
         count += 1
   return count
```

This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.
Now we can call it for our file.

```py
filename = input("Enter a filename: ")
with open(filename) as f:
   text = f.read()
print(count_char(text, "r")

# Result:

>>>
Enter a filename: analyzed_text.txt
83
```

*The character "r" appears 83 times in the file.*  

The next part of the program finds what percentage of the text each character of the alphabet occupies.

```py
for char in "abcdefghijklmnopqrstuvwxyz":
   perc = 100 * count_char(text, char) / len(text)
   print("{0} - {1}%".format(char, round(perc, 2)))
```

Let's put it all together and run the program:  

```py
def count_char(text, char):
   count = 0
   for c in text:
      if c == char:
         count +=1
   return count

filename = input("Enter a filename: ")
with open(filename) as f:
   text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
   perc = 100 * count_char(text, char) / len(text)
   print("{0} - {1}%".format(char, round(perc, 2)))

# Result:

Enter a filename: test.txt
a - 4.68%
b - 4.94%
c - 2.28%
...
```

### Module 5 Quiz

You **CAN** slice a tuple.  #FIX (try slice a tuple)  

## Functional Programming

---

Functional programming is a style of programming that (as the name suggests) is based around functions.
A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous lesson on functions as objects. Higher-order functions take other functions as arguments, or return them as results.  
**Example:**

```py
def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))

# Result:
>>>
20
>>>
```

*The function apply_twice takes another function as its argument, and calls it twice inside its body.*

### Pure Functions

Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.
This is how functions in math work: for example, The cos(x) will, for the same value of x, always return the same result.
Below are examples of pure and impure functions.  
**Pure function:**

```py
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
```

**Impure function:**

```py
some_list = []

def impure(arg):
  some_list.append(arg
```

*The function above is not pure, because it changed the state of some_list.*  

Using pure functions has both advantages and disadvantages.  
Pure functions are:  

* easier to reason about and test.
* more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
* easier to run in parallel.  
  
The **main disadvantage** of using only pure functions is that they majorly complicate the otherwise simple task of I/O, since this appears to inherently require side effects.
They can also be more difficult to write in some situations.

### Lambdas

Creating a function normally (using **def**) assigns it to a variable automatically.
This is different from the creation of other objects - such as strings and integers - which can be created on the fly, without assigning them to a variable.
The same is possible with functions, provided that they are created using lambda syntax. Functions created this way are known as **anonymous**.
This approach is most commonly used when passing a simple function as an argument to another function. The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.

```py
def my_func(f, arg)
   return f(arg)
my_func(lambda x: 2*x*x, 5) # First argument is lambda function
```

*Lambda functions get their name from lambda calculus, which is a model of computation invented by Alonzo Church.*

Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression - usually equivalent to a single line of code.  
**Example:**

```py
# named function
def polynomial(x):   # англ. многочлен
   return x**2 + 5 * x + 4
print(polinomial(-4))

# OR Lambda

print((lambda x: x**2 + 5*x + 4)(-4))

#Result:
>>>
0
0
>>>
```

*In the code above, we created an anonymous function on the fly and called it with an argument.*  

Lambda functions can be assigned to variables, and used like normal functions.

```py
double = lambda x: x * 2
print(double(7))

# Result:
>>>
14
>>>
```

*However, there is rarely a good reason to do this - it is usually better to define a function with def instead.*  

### Map & Filter

The built-in functions **map** and **filter** are very useful higher-order functions that operate on lists (or similar objects called **iterables**).

#### Map

The function **map** takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

**Example:**  

```py
def add_five(x):
   return x + 5

nums = [11, 22, 33, 44, 55]
resutl = list(map (add_five, nums))
print(result)

# Result
>>>
[16, 27, 38, 49, 60]
>>>
```

We could have achieved the same result more easily by using lambda syntax.

```py
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x + 5, nums))
print(result)

# Resutl
>>>
[16, 27, 38, 49, 60]
>>>
```

*To convert the result into a list, we used list explicitly.*

#### Filter

The function **filter** filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).

**Example:**

```py
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

# Result:
>>>
[22, 44]
>>>
```

*Like **map**, the result has to be explicitly (явно) converted to a list if you want to print it.*

### Generators

Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with **for** loops.
They can be created using functions and the **yield** statement.

**Example:**

```py
def countdown():
    i = 5
    while i > 0:
        yield i # -- англ гл. produce or provide. Почти как return
        i -= 1

for i in countdown():
    print(i)

# Result:
>>>
5
4
3
2
1
>>>
```

*The **yield** statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.*

Due to the fact that they **yield** one item at a time, generators don't have the memory restrictions of lists.
In fact, they can be **infinite**!

```py
def infinite_sevens():
    while True:
        yield 7

for i in infinite_sevens():
    print(i)
```

*In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.*

Finite generators can be converted into lists by passing them as arguments to the list function.

```py
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

# Result:
>>>
[0, 2, 4, 6, 8, 10]
>>>
```

*Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been generated before we start to use them.*

### Decorators

**Decorators** provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you don't want to modify.  
**Example:**

```py
def decor(func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()
```

We defined a function named **decor** that has a single parameter **func**. Inside **decor**, we defined a nested function named **wrap**. The wrap function will print a string, then call **func()**, and print another string. The **decor** function returns the **wrap** function as its result.
We could say that the variable **decorated** is a decorated version of **print_text** - it's **print_text** plus something.
In fact, if we wrote a useful decorator we might want to replace **print_text** with the decorated version altogether so we always got our "plus something" version of **print_text**.
This is done by re-assigning the variable that contains our function:

```py
print_text = decor(print_text)
print_text()
```

*Now print_text corresponds to our decorated version.*

We decorated our function by replacing the variable containing the function with a wrapped version.

```py
def print_text():
    print("Hello Lord!")

print_text = decor(print_text)
```

This pattern can be used at any time, to wrap any function.
Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
If we are defining a function we can "decorate" it with the @ symbol like:

```py
@decor
def print_text():
    print("Helllllow my Lord!")
```

This will have the same result as the above code.  
*A single function can have multiple decorators.*

### Recursion

Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference - functions calling themselves. It is used to solve problems that can be broken up into easier sub-problems of the same type.

A classic example of a function that is implemented recursively is the factorial function, which finds the product of all positive integers below a specified number.
For example, 5! (5 factorial) is 5 \* 4 \* 3 \* 2 \* 1 (120). To implement this recursively, notice that 5! = 5 \* 4!, 4! = 4 \* 3!, 3! = 3 \* 2!, and so on. Generally, n! = n \* (n-1)!.
Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials.
Below is a recursive implementation of the factorial function.

```py
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x -1)

print(factorial(5))

# Result: 120
```

*The **base case** acts as the exit conditiona of the recursion*

Recursive functions can be infinite, just like infinite **while** loops. These often occur when you forget to implement the base case.

Below is an incorrect version of the factorial function. It has no base case, so it runs until the interpreter runs out of memory and crashes.

```py
def factorial(x):
     return x * factorial(x - 1)

factorial(5)

# Result:
RuntimeError: maximum recursion depth exceeded
```

Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.  
**Example:**

```py
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)

def is_odd(x):
    return not is_even(x)

    print(is_odd(17))
    print(is_even(23))

# Result
True
False
```

### Sets

---

**Sets** are data structures, similar to lists or dictionaries. They are created using curly braces, or the **set function**. They share some functionality with lists, such as the use of in to check whether they contain a particular item.

```py
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set) # True
print("spam" not in word_set) # False
```

*To create an empty set, you must use set(), as {} creates an empty dictionary.*

Sets differ from lists in several ways, but share several list operations such as **len**.

* They are unordered, which means that they can't be indexed.
* They **cannot** contain **duplicate** elements.
* Due to the way they're stored, it's **faster** to check whether an item is part of a set, rather than part of a list.
* Instead of using **append** to add to a set, use **add**.
* The method remove removes a specific element from a set; pop removes an arbitrary element.

```py
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print("There is a set nums: ", nums) # There is no dupliacate 1 element
nums.add(-7) # add -7 element
nums.remove(3) # remove 3 element
print("There is a changed set nums", nums)

# Result:
{1, 2, 3, 4, 5, 6}
{1, 2, 4, 5, 6, -7}
```

*__Basic__ uses of sets include membership testing and the elimination of duplicate entries.*

Sets can be combined using mathematical operations.

* The **union** operator | combines two sets to form a new one containing items in either.
* The **intersection** operator & gets items only in both.
* The **difference** operator - gets items in the first set but not in the second.
* The **symmetric difference** operator ^ gets items in either set, but not both.

```py
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second) # union
print(first & second) # intersection
print(first - second) # difference
print(second - first) # difference
print(first ^ second) # symmetryc difference

# Result:
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{4, 5, 6}
{1, 2, 3}
{8, 9, 7}
{1, 2, 3, 7, 8, 9}
```

### Data Structures

As we have seen in the previous lessons, Python supports the following data structures: **lists, dictionaries, tuples, sets.**

**When to use a dictionary**:

* When you need a logical association between a key:value pair.
* When you need fast lookup for your data, based on a custom key.
* When your data is being constantly modified. Remember, **dictionaries are mutable**.

**When to use the other types:**

* Use **lists** if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
* Use a **set** if you need uniqueness for the elements.
* Use **tuples** when your data cannot change.

*Many times, a **tuple** is used in combination with a **dictionary**, for example, a **tuple** might represent a key, because it's immutable.*

### itertools

The module itertools is a standard library that contains several functions that are useful in functional programming.
One type of function it produces is infinite iterators.

* The function **count** counts up infinitely from a value.
* The function **cycle** infinitely iterates through an iterable (for instance a list or * string).
* The function **repeat** repeats an object, either infinitely or a specific number of times.  
**Example:**

```py
from itertools import count, cycle, repeat

for i in count(3):
    print(i)
    if i >= 11:
        break
```

There are many functions in **itertools** that operate on iterables, in a similar way to **map** and **filter**.  
Some examples:  

* **takewhile** - takes items from an iterable while a predicate function remains true;
* **chain** - combines several iterables into one long one;
* **accumulate** - returns a running total of values in an iterable.

```py
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

# Result:
[0, 1, 3, 6, 10, 15, 21, 28]
[0, 1, 3, 6]
```

There are also several combinatoric functions in itertool, such as product and permutation.
These are used when you want to accomplish a task with all possible combinations of some items.  
**Example:**

```py
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

letters_permute = list(permutations(letters))
print("letters permutable", letters_permute[1])

# Result:
[('A', 0), ('A', 1), ('B', 0), ('B', 1)]
[('A', 'B'), ('B', 'A')]
letters permutable ('B', 'A')
```

Module 6 Quiz
