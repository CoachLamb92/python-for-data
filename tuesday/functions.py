# Equivalents in named function and lambda
def sum(a, b):
    return a + b

sum_lambda = lambda a, b: a + b

# Making flexible functions

def multiplier(n):
    return lambda x: x * n

doubler = multiplier(2)
tripler = multiplier(3)

# print(doubler(10))
# print(tripler(10))

numbers = [2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))

# print(doubled)

numbers = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))
# print(evens)
# print(odds)

# sort
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort(key=lambda x: abs(x-8))
print(numbers)
numbers.sort(reverse= True, key=lambda x: abs(x-8))
print(numbers)

# reduce
from functools import reduce
numbers_2 = list(range(1, 6))
result = reduce(lambda x, y: x * y, numbers_2)
print(result)