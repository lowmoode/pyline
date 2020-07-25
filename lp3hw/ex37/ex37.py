"""
Here I write keywords I want to remeber

as - Part of the with-as statement.
with - With an expression as a variable do.
Example:
with X as Y: pass

This creates a temporary variable (often called f), which is only 
accessible in the indented block of the with statement.
"""
with open("sometext.txt") as f:
    print(f.read())

# -----------------------------

# assert - Assert (ensure) that something is true.

# break - Stop this loop right now.

# try - try this block, and if exception, go to except.

"""
exept - if an exception happiencs, do this
        use try-except statement """

try:
  print(1)
  assert 2 + 2 == 5 # Not True
except AssertionError:
  print(3)
except:# ----- Не сработает потому что исключения все закончились
  print(4)


# yeld - Pause here and return to caller
# Example: def X(): yeld Y; X().next()


def infinite_sevens():
    yield 7

for i in infinite_sevens():
    print(i)
