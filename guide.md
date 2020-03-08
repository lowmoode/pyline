
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
