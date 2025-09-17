import numpy as np

numbers = [1, 2, 3, 4]
array = np.array(numbers)

print(array)
# [1 2 3 4]

doubled = array * 2
print(doubled)
# [2 4 6 8]

zeros = np.zeros((2, 3))
print(zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]

ones = np.ones((3))
print(ones)
# [1. 1. 1.]

range_array = np.arange(0, 10, 2)
print(range_array)
# [0 2 4 6 8]

single_digits = np.arange(0, 10)
print(single_digits)
# [0 1 2 3 4 5 6 7 8 9]

sixteen_ones = np.ones((4, 4))
print(sixteen_ones)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

even_spread = np.linspace(0, 1, 7)
print(even_spread)
# [0.   0.16666667 0.33333333 0.5   0.66666667 0.83333333 1.  ]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print("Should be 2:", matrix[0, 1])
# Should be 2: 2
print("Should be 2:", matrix[0][1])
# Should be 2: 2

print("Every second number from each row:", matrix[:, 1])
# Every second number from each row: [2 5 8]

print("The last number in each row:", matrix[:, -1])
# The last number in each row: [3 6 9]

numbers = np.arange(1, 11)
half_numbers = numbers[:5]
print(half_numbers)
# [1 2 3 4 5]

top_two_rows = matrix[:2]
print(top_two_rows)
# [[1 2 3]
#  [4 5 6]]

mini_matrix = matrix[-2:, -2:]
print(mini_matrix)
# [[5 6]
#  [8 9]]
