from random import randint

def mini_sprint_1(first):
    def difference_of_squares(num_1, num_2):
        return abs((num_1 ** 2) - (num_2 ** 2))

    def sum_of_nums(num_1, num_2):
        return num_1 + num_2
    
    options = [first+1, first-1]
    second = options[randint(0, 1)]
    output_1 = difference_of_squares(first, second)
    output_2 = sum_of_nums(first, second)

    print(f"The difference between the squares of consecutive numbers ({first} and {second}) is equal to the sum of {first} and {second}")
    print(f"Difference of squares: {output_1}")
    print(f"Sum of numbers: {output_2}")

# mini_sprint_1(3)
# mini_sprint_1(10)

def challenge_1():
    def my_first_function(item):
        print(f"I love {item}")

    my_first_function("sausages")
    my_first_function("Hollow Knight")

# challenge_1()

def challenge_2():
    def tripler(num):
        return num * 3

    for var in [3, 10, 50]:
        print(tripler(var))

# challenge_2()

def challenge_3():
    def greeter(name):
        return f"Hello {name}!"

    print(greeter("Georgie"))

# challenge_3()

def challenge_4():
    def is_even(num):
        return "Odd" if num % 2 else "Even"

    print(is_even(1))
    print(is_even(2))

# challenge_4()

def challenge_5():
    def repeat_word(word, times):
        return word * times

    print(repeat_word("hi", 3))
    print(repeat_word("dog", 5))

# challenge_5()

def challenge_6():
    def factorial(n):
        result = 1
        if n:
            for var in list(range(2, n+1)):
                result *= var
        return result
    
    print(factorial(3))
    print(factorial(5))
    print(factorial(1))
    print(factorial(0))

# challenge_6()

def challenge_7():
    def power(base, exponent = 2):
        return base ** exponent

    print(power(3))
    print(power(5))
    print(power(4, 3))
    print(power(10, 6))

# challenge_7()

def challenge_8():
    from math import pi
    cicumference_lambda = lambda r: 2 * pi * r
    area_lambda = lambda r: pi * r ** 2

    print(cicumference_lambda(10))
    print(area_lambda(10))

# challenge_8()

def challenge_9():
    triangle_area_2 = lambda a, b, c: (((a + b + c) / 2) * (((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c)) ** 0.5

    print(triangle_area_2(3, 4, 5))

# challenge_9()

def challenge_10():
    import csv
    data = []
    with open("tuesday/states.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    for datum in data:
        match datum["State"]:
            case "VIC":
                datum["Abbr."] = "VIC"
                datum["State"] = "Victoria"
                datum["Capital"] =  "Melbourne"
            case "NSW":
                datum["Abbr."] = "NSW"
                datum["State"] = "New South Wales"
                datum["Capital"] =  "Sydney"
            case "SA":
                datum["Abbr."] = "SA"
                datum["State"] = "South Australia"
                datum["Capital"] =  "Adelaide"
            case "WA":
                datum["Abbr."] = "WA"
                datum["State"] = "Western Australia"
                datum["Capital"] =  "Perth"
            case "TAS":
                datum["Abbr."] = "TAS"
                datum["State"] = "Tasmania"
                datum["Capital"] =  "Hobart"
            case "QLD":
                datum["Abbr."] = "QLD"
                datum["State"] = "Queensland"
                datum["Capital"] =  "Brisbane"
            case "ACT":
                datum["Abbr."] = "ACT"
                datum["State"] = "Australian Capital Territory"
                datum["Capital"] =  "Canberra"
            case "NT":
                datum["Abbr."] = "NT"
                datum["State"] = "Northern Territory"
                datum["Capital"] =  "Darwin"
    
    header = list(data[0].keys())

    with open("tuesday/states.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for datum in data:
            writer.writerow({
                'State': datum["State"],
                'Population': datum["Population"],
                'Abbr.': datum["Abbr."],
                'Capital': datum["Capital"]}
            )

# challenge_10()

def challenge_11():
    import csv
    data = []
    with open("tuesday/states.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    total_pop = sum([int(row["Population"]) for row in data])
    print(total_pop)

# challenge_11()
 