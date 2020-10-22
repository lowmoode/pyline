numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]
print(*more_numbers, sep=', ')

numbers = [2, 1, 3, 4, 7]
more_numbers = [numbers, 11, 18]
print(*more_numbers, sep=', ')

# ------------- 

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits[0], fruits[1], fruits[2], fruits[3])

print(*fruits) #разница заметна

# -----------------

def transpose_list(list_of_lists):
    print (*list_of_lists)
    return [
        list(row) for row in zip(*list_of_lists)
    ]

"""

>>> transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

transposed_list = transpose_list([[1,2,3], [4,5,6], [7,8,9]])

print(transposed_list)
