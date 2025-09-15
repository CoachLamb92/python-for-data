def mini_sprint_1():
    favourite_food = "sausages"
    birth_year = 1992
    print(f"I was born in {birth_year} and my favorite food is {favourite_food}.")

# mini_sprint_1()

def mini_sprint_2():
    my_variables = [7, 0.99, "ice-cream", False]
    for var in my_variables:
        print(f"Var: {var}{(10-len(str(var)))* " "} | Type: {type(var)}{(15-len(str(type(var))))* " "} | Size in bytes: {var.__sizeof__()}")

# mini_sprint_2()

def mini_sprint_3():
    user_age = int(input("Please enter your age: "))
    print(f"You are {user_age} years old!")
    print()
    user_decimal = float(input("Please enter a decimal: "))
    print(user_decimal)

# mini_sprint_3()

def mini_sprint_4():
    num_1 = int(input("Please enter a number: "))
    num_2 = int(input("Please enter another number: "))
    sum_of_nums = num_1 + num_2
    print(sum_of_nums)
    print(sum_of_nums * "cat")
    print(f"10 is greater than 5: {10 > 5}")

# mini_sprint_4()

def challenge_1():
    """
    Use input() to grab a number value from the user and cast it to a float.
    Divide the new float by any number and cast the result to an int.
    Use input() to grab the name of a user and print "Hello [name]!".
    """
    user_input = float(input("Enter a number: "))
    divisors = {2, 3, 4, 5}
    divisor = divisors.pop()
    result = user_input / divisor
    user_name = input("Who even are you?\n")
    print(f"Hello {user_name}!\nWe took your number and divided it by {divisor} to get {result}.\nCasting this to an integer results in: {int(result)}")

challenge_1()

def challenge_2():
    """
    Grab a number value height from the user and store it as an int.
    Grab a number value width from the user and store it as an int.
    Print the area of a rectangle using the provided height and width.
    """
    width = int(input("Enter a number: "))
    height = int(input("Enter another number: "))
    print(f"The area of a rectangle with a width of {width} and a height of {height} is: {width*height}")
    for i in range(height):
        print("*" * width)

challenge_2()