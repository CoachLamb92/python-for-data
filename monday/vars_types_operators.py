# Python Basics

# Variables

# Assigning values to variables
x = 10 # int (integer)
name = "Morgan" # str (string)
is_happy = True # bool (boolean)

# Using variables
print(x)
print("Hello", name)
print("Are you happy?", is_happy)

# Reassiging values
x = 20
print("Now x is:", x)

# Memory concept
my_number = 5
print(my_number) # 5

my_number = my_number + 3
print(my_number) # 8

# Types Code-along
# import sys # allows us to check the memory size of an object

# Integer
num_1 = 1
print(num_1)
print(type(num_1))
# print(sys.getsizeof(num_1)) # 28 bytes
print(num_1.__sizeof__()) # 28 bytes also

# Float
float_1 = 1.0
print(type(float_1)) # float
print(float_1.__sizeof__()) # 24 bytes

# String
str_1 = "1"
print(type(str_1)) # str
print(str_1.__sizeof__()) # 42 bytes

# Boolean
bool_1 = True
print(type(bool_1)) # bool
print(bool_1.__sizeof__()) # 28 bytes

# Casting (Type Conversion)

# Casting means changing one type into another
# You CAN convert between compatible types (e.g. int --> float, bool --> int)
# You CANNOT convert directly between incompatible types (e.g. "hello" --> int)

# Casting examples
my_num = 5
my_float = float(my_num) # 5.0
print(my_float)

my_str = "123"
my_int = int(my_str) # works if string is numeric
print(my_int)

# Arithmetic and Comparison operators

