
# Python

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

___

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

Once a file has been opened and used, you should close it.
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
