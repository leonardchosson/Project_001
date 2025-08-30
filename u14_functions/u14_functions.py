
###################################################
# Part 1: Learning Exercises

# Exercise 1: A Simple Function
# Define a function that prints "Hello, World!" and call it.

#### stores the function in computer memory
def hello():
    print("Hello, world.")
    print("bye")

# call the function
# hello()



#------------------------------------------------------------
# Exercise 2: Function with One Parameter
# Define a function that takes a name as a parameter and greets the user.

# age = 10
# # my age is 10 years old
# print("my age is", age, "years old")
# print(f"my age is {age} years old.")



# Call the function with your name.
def greeting(name): # "variable" >>> parameter
    print(f"Hello, {name}")

greeting("Ranen")
greeting("Heng Hyi")


#------------------------------------------------------------
# Exercise 3: Function with Two Parameters
# Define a function that takes two numbers and prints their sum.
# def add_numbers(num1, num2):
#     print("The sum of {} and {} is {}".format(num1, num2, num1 + num2))

# # Call the function with two numbers.
# add_numbers(5, 10)

def addnum(num1,num2):
    ans = num1 + num2
    print(num1,"+", num2, "=", ans)
addnum(600,40)


#------------------------------------------------------------
# Exercise 4: Function with a Return Value
# Define a function that calculates the area of a rectangle.
# def calculate_area(length, width):
#     return length * width

# # Call the function and store the result.
# area = calculate_area(5, 3)
# print("The area of the rectangle is {}".format(area))

# def area_triangle(base, height):
#     area = base * height
#     print(area)
# area_triangle(3,4)


# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# def iseven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# for i in list1:
#     if iseven(i) == True:
#         print(i, "is even")
#     else:
#         print(i ,"is odd")

        

#------------------------------------------------------------
# Exercise 5: Using Returned Values in Further Computations
# Define a function that calculates the perimeter of a rectangle.
# def calculate_perimeter(length, width):
#     return 2 * (length + width)

# # Use both functions to calculate the area and perimeter.
# length = 6
# width = 4
# area = calculate_area(length, width)
# perimeter = calculate_perimeter(length, width)
# print("For a rectangle of length {} and width {}:".format(length, width))
# print("Area: {}, Perimeter: {}".format(area, perimeter))





#------------------------------------------------------------
# Exercise 6: Demonstrating Local and Global Variables
# Define a function that modifies a local variable.
# def local_variable_example():
#     x = 10  # Local variable
#     print("Inside the function, x is {}".format(x))

# # Outside the function.
# x = 20  # Global variable
# local_variable_example()
# print("Outside the function, x is {}".format(x))






#------------------------------------------------------------




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.


# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])

# def greet_users(namelst):
#     for i in namelst:
#         print("hello",i)

# greet_users(["yes", "ok"])

#------------------------------------------------------------
# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.


# Test the function with multiple operations.
# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))

def calculator(a,b,c):
    if c == "+":
        total = a + b
    elif c == "-":
        total = a - b
    elif c == "*":
        total = a * b
    elif c == "/":
        total = a / b
    return total

print(calculator(3,2,"+"))


#------------------------------------------------------------
# Exercise 9: Palindrome Checker
# Write a function that checks if a string is a palindrome.


# Test the function with different words.
# print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))


words = [
    "level", "racecar", "orange", "radar", "banana", "civic", "refer",
    "apple", "madam", "kayak", "robot", "reviver", "noon", "pop", "deed",
    "book", "wow", "mirror", "eye", "nope", "rotor", "stats", "hello", 
    "toot", "peep", "school", "mum", "dad", "gig", "noon",
    "python", "coding", "class", "student", "lesson", "computer", "keyboard",
    "monitor", "window", "projector", "teacher", "laptop", "science", "library",
    "pencil", "marker", "whiteboard", "homework", "question", "answer"
]
def palindrome_checker(i):
    if i.flip() == i:
        return True
    else:
        return False
    
for a in words:
    print(palindrome_checker(a))



#------------------------------------------------------------
# Exercise 10: Display Multiplication Table
# Write a function that takes a number and prints its multiplication table.

# Call the function with a number.
# multiplication_table(5)






#------------------------------------------------------------