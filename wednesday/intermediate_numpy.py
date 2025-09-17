import numpy as np

numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)
print(matrix)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

middle_cols = matrix[:,1:3]
print(middle_cols)
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

new_array = middle_cols.flatten()
print(new_array)
# [ 2  3  6  7 10 11]

a = np.arange(1, 5)
b = np.arange(10, 50, 10)
print(a, b)
# [1 2 3 4] [10 20 30 40]

print(a + b)
# [11 22 33 44]

print(b - a)
# [ 9 18 27 36]

print(b * a)
# [ 10  40  90 100]

print(b / a)
# [10. 10. 10. 10.]

print(np.sqrt(a))
# [1.   1.414 1.732 2.  ]

c = np.array([5, 10, 15])
d = np.array([2, 4, 6])
product = c * d
division = c / d
summed = c + d
subtraction = c - d
print(f"Product: {product}")
print(f"Division: {division}")
print(f"Sum: {summed}")
print(f"Subtraction: {subtraction}")
# Product: [10 40 90]
# Division: [2.5 2.5 2.5]
# Sum: [ 7 14 21]
# Suubstraction: [3 6 9]

cubed = c**3
print(cubed)
# [ 125 1000 3375]

array = np.array([2, 4, 6, 8])
half_array = array * 0.5
print(half_array)
# [1. 2. 3. 4.]

matrix = np.array([[7, 8, 9],[4, 5, 6],[1, 2, 3]])
summation = matrix + np.array([1, 2, 3])
print(summation)
# [[ 8 10 12]
#  [ 5  7  9]
#  [ 2  4  6]]

matrix = np.array([[4, 5, 6],[1, 2, 3]])
summation = matrix + 10
print(summation)
# [[14 15 16]
#  [11 12 13]]