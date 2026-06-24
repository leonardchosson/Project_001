#------------------------------------------------------------
# For Loops through List
#------------------------------------------------------------

# Exercise 1: Printing Items (Method 1)
# Given fruits = ["apple", "banana", "cherry"]
# Use a for loop to print each fruit directly.
# Output example:
# I like to eat apple.
# I like to eat banana.
# I like to eat cherry.


# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print("I like to eat", i + ".")




#------------------------------------------------------------
# Exercise 2: Printing Items (Method 2)
# Given the same fruits list
# Use for i in range(len(fruits)) to print the items.
# Output example:
# Fruit 1: apple
# Fruit 2: banana
# Fruit 3: cherry

# fruits = ["apple", "banana", "cherry"]
# for i in range(len(fruits)):
#     print("Fruit", i + 1, ":", fruits[i])



#------------------------------------------------------------
# Exercise 3: Numbers Greater than 50
given_numbers = [12, 67, 45, 89, 23]
# Use a for loop to print only numbers greater than 50.
# Expected Output:
# 67
# 89

# for i in given_numbers:
#     if i > 50:
#         print(i)


#------------------------------------------------------------
# For Loops through Dictionary
#------------------------------------------------------------

# Exercise 4: Printing Keys
# Given scores = {"Ali": 55, "Bala": 80, "Cindy": 62}
# Write a loop to print all the student names.
# Expected Output:
# Ali
# Bala
# Cindy
# scores = {"Ali": 55, "Bala": 80, "Cindy": 62}
# for i in scores:
#     print(i)




#------------------------------------------------------------
# Exercise 5: Printing Values
# Using the same dictionary, print only the marks.
# Expected Output:
# 55
# 80
# 62
# for i in scores:
#     print(scores[i])




#------------------------------------------------------------
# Exercise 6: Keys and Values Together
# Print each student’s name and score in the format:
# Ali scored 55
# Bala scored 80
# Cindy scored 62

# for i in scores:
#     print(i, "scored", scores[i])


#------------------------------------------------------------
# For Loops with Nested Lists
#------------------------------------------------------------

# Exercise 7: Mapping Students to Scores
students = ["Ali", "Bala", "Cindy"]
marks = [55, 80, 62]
# Use a for loop to combine them into a dictionary.
# Expected Output:
# {"Ali": 55, "Bala": 80, "Cindy": 62}
student_marks = {} # don't use dict as variable name

# for i in range(len(students)):
#     student_marks[students[i]] = marks[i]
# print(student_marks)
#------------------------------------------------------------
# Exercise 8: Pairing Names
boys = ["Tom", "Dick"]
girls = ["Amy", "Beth"]
# Make a dictionary matching each boy to each girl.
# Expected Output:
# {"Tom": "Amy", "Dick": "Beth"}
boys_girls = {}

# for i in range(len(boys)):
#     boys_girls[boys[i]] = girls[i]
# print(boys_girls)


#------------------------------------------------------------
# Exercise 9: Totaling Scores
subjects = ["Math", "Science", "English"]
marks = [75, 82, 68]
# Store into a dictionary, then loop to calculate total.
# Expected Output:
# Total Score = 225

# print(sum(marks))

#------------------------------------------------------------
# While Loop Validation
#------------------------------------------------------------

# Exercise 10: Length Check
# Keep asking user for a username until it has at least 5 characters.

# username = ""
# while len(username)<5:
#     username = input("input a usename that has at least 5 characters")



# ----------------------------------------------------------------

# Exercise 11: Numbers Only
# Keep asking user to enter age until input contains digits only.
age = "r"

# while True:
#     age = input("enter an age that only contains numbers. ")    #17
#     if age.isdigit():
#         break
# ----------------------------------------------------------------

# Exercise 12: Uppercase Only
# Keep asking until user enters a code in uppercase letters only.


# while True:
#     code =input("enter a code with upercase letters only ")
#     if code.isupper():
#         break


# ----------------------------------------------------------------

# Exercise 13: Lowercase Only
# Keep asking until user enters an email in lowercase only.


# while True:
#     code = input("Enter an email which only contains lowercase letters. ")
#     if code.islower():
#         break


# ----------------------------------------------------------------

# Exercise 14: Password Validation
# Keep asking until user enters a password with length >= 8.


# while True:
#     password = input("Enter a password with more than 8 characters. ")
#     if len(password) >= 8:
#         break


# ----------------------------------------------------------------

# Exercise 15: Date Validation
# Keep asking until user enters a date in format MM-YYYY.
# Ensure the date is between 01-1900 and 12-2025.
# i = 'MM-YYYY'

# print(i[:-3] in range(1,12))
# # def validation(i):
# while True:
#     if i[:-3].isdigit() and i[2] == "-" and i[3:7].isdigit and len(i) == 7:
#         if i[:-3] in ra:
        
#------------------------------------------------------------
# Adding to and Deleting from List
#------------------------------------------------------------

# Exercise 16: Adding Numbers
# Start with empty list even_numbers = []
numbers = [3, 8, 12, 7, 10]
# Add only even numbers into even_numbers.
# Expected Output:
# [8, 12, 10]
# even_num = []
# for i in numbers:
#     print(i)
#     if i%2 == 0:
#         even_num.append(i)
# print(even_num)




# ----------------------------------------------------------------

# Exercise 17: Copy Names with 'A'
names = ["Ali", "Ben", "Amy", "John"]
# Copy only names starting with 'A' into a new list.
# Expected Output:
# ["Ali", "Amy"]
# A_names = []
# for i in names:
#     if i.startswith("A"):
#         A_names.append(i)
# print(A_names)


# ----------------------------------------------------------------

# Exercise 18: Copy Scores > 50
scores = [23, 56, 78, 49, 88]
# Copy all scores above 50 into pass_list.
# Expected Output:
# [56, 78, 88]
# pass_list = []
# for i in scores:
#     if i>50:
#         pass_list.append(i)
# print(pass_list)


# ----------------------------------------------------------------

# Exercise 19: Remove Odd Numbers
numbers = [12, 7, 15, 20, 33]
# Delete all odd numbers.
# Expected Output:
# [12, 20]

# for i in numbers:
#     if i%2 !=0:
#         numbers.remove(i)
# print(numbers)


# ----------------------------------------------------------------

# Exercise 20: Remove Names with 'x'
names = ["Alex", "Max", "Sam"]
# Delete names that contain 'x'.
# Expected Output:
# ["Sam"]
# namel = []
# for i in names:
#     if "x" not in i:
#         namel.append(i)
# print(namel)


# ----------------------------------------------------------------

# Exercise 21: Remove Fail Scores
marks = [12, 35, 50, 67, 88]
# Remove all scores below 50.
# Expected Output:
# [50, 67, 88]

# marks = [12, 35, 50, 67, 88]
# marks2 = marks.copy()

# for m in marks2: # looping through the copy
#     if m < 50:
#         marks.remove(m) # removing from original

# marks2 = []

# for m in marks:
#     if m >= 50:
#         marks2.append(m)

# replace_list = []

# for i in marks:
#     if i<50:
#         replace_list.append(i)
#     for i in replace_list:
#         marks.remove(i)
# print(marks)



#------------------------------------------------------------
# String and List Functions
#------------------------------------------------------------

# Exercise 22: find()
sentence = "Computing is fun"
# Find the index of "is".
# Expected Output:
# 10

# print(sentence.find("is"))



# ----------------------------------------------------------------

# Exercise 23: find() not found
# sentence = "I love Python"
# Use find() to check if "Java" exists.
# Expected Output:
# -1





# ----------------------------------------------------------------

# Exercise 24: index()
# numbers = [10, 20, 30, 40]
# Find the position of number 30.
# Expected Output:
# 2





# ----------------------------------------------------------------

# Exercise 25: index() Error
# numbers = [1, 2, 3]
# What happens if you use index() on 9?
# Expected: ValueError (9 is not in list)




#------------------------------------------------------------
# String Slicing
#------------------------------------------------------------

# Exercise 26: First 3 Letters
# word = "Computing"
# Extract first 3 characters.
# Expected Output:
# Com





# ----------------------------------------------------------------

# Exercise 27: Username
# name = "John Malkovich"
# Extract first 5 characters as username (lowercase).
# If first name is shorter than 5 chars, use letters from last name.
# Remove spaces before slicing.
# Example: "John Malkovich" → "johnm"
# Example: "Samson Gorbachov" → "samso"





# ----------------------------------------------------------------

# Exercise 28: Reverse String
# word = "Python"
# Print string in reverse.
# Expected Output:
# nohtyP





# ----------------------------------------------------------------




#------------------------------------------------------------
# List Slicing
#------------------------------------------------------------

# Exercise 29: First 3 Items
# numbers = [2, 4, 6, 8, 10]
# Extract first 3 items.
# Expected Output:
# [2, 4, 6]





# ----------------------------------------------------------------

# Exercise 30: Last 2 Items
# From the same list, extract last 2 items.
# Expected Output:
# [8, 10]





# ----------------------------------------------------------------

# Exercise 31: Middle Items
# Extract the middle 3 items.
# [2, 4, 6, 8, 10] → [4, 6, 8]
# [2, 4, 6, 8, 10, 12, 14] → [6, 8, 10]





# ----------------------------------------------------------------




#------------------------------------------------------------
# ASCII, chr(), ord()
#------------------------------------------------------------

# Exercise 32: ord() Value
# Find ASCII value of 'A' and 'z'.
# Expected Output:
# 65
# 122

# print(ord(65))
# print(ord(122))


# ----------------------------------------------------------------

# Exercise 33: Generate Password
# Use chr() to generate a password of random ASCII characters.
# Password rules:
# - At least 2 uppercase (65–90)
# - At least 2 lowercase (97–122)
# - At least 2 digits (48–57)
# - At least 2 special characters (33–47, 58–64, 91–96, 123–126)
import random

password = ""
for i in range(2):
    # Uppercase letters (A–Z)
    password += chr(random.randint(65, 90))
    # Lowercase letters (a–z)
    password += chr(random.randint(97, 122))
    # Digits (0–9)
    password += chr(random.randint(48, 57))

    # Special characters
    randval = random.randint(1, 4)
    if randval == 1:
        password += chr(random.randint(33, 47))
    elif randval == 2:
        password += chr(random.randint(58, 64))
    elif randval == 3:
        password += chr(random.randint(91, 96))
    else:
        password += chr
# ----------------------------------------------------------------

# Exercise 34: Checksum
sentence = "ABCDEFG"
# Add up ASCII values of all characters.
# checksum = total % 256
# Example 1: "ABCDEFG" → 65+66+67+68+69+70+71 = 476 → 476 % 256 = 220
# Example 2: "Today is Sunday!" → 1458 % 256 = 178
# total = 0
# for i in sentence:
#     total+=ord(i)
# print(total%256)




#------------------------------------------------------------
# Functions
#------------------------------------------------------------

# Exercise 35: Define and Call
# Write a function greet(name) that prints:
# "Hello, {name}, welcome to Computing!"
# Example call: greet("Ali")
# Expected Output:
# Hello, Ali, welcome to Computing!

def greet



# ----------------------------------------------------------------

# Exercise 36: Function with Parameter
# Define a function square(n) that returns n squared.
# Example call: square(5)
# Expected Output:
# 25





# ----------------------------------------------------------------

# Exercise 37: Function with 2 Parameters
# Define a function add(x, y) that returns the sum.
# Example call: add(12, 8)
# Expected Output:
# 20





# ----------------------------------------------------------------

# Exercise 38: Using Function
# Write a function average(lst) that returns the mean of a list of numbers.
# Example call: average([10, 20, 30, 40, 50])
# Expected Output:
# 30.0





# ----------------------------------------------------------------

# Exercise 39: Reuse Function with List
# Reuse your add(x, y) function.
# Write a program that accepts a list of numbers and calculates total sum.
# Example call: [5, 10, 15, 20]
# Expected Output:
# 50





# ----------------------------------------------------------------
# Exercise 40: Packing with Floor Division and Modulus
# Write a function pack_items(total_items, box_size) that:
# - Calculates how many full boxes can be filled (//).
# - Calculates leftover items (%).
# Example call: pack_items(257, 7)
# Expected Output:
# 36 full boxes, 5 items leftover



#------------------------------------------------------------
# File I/O
#------------------------------------------------------------

# Exercise 41: Writing to File
# Write "Hello Computing Students" into a file named test.txt.
# Expected Content (test.txt):
# Hello Computing Students

# sentence = "Hello Computing Students"

# write this sentence to a file



# ----------------------------------------------------------------

# Exercise 42: Reading from File
# Read contents of test.txt and display.
# Expected Output:
# Hello Computing Students





# ----------------------------------------------------------------
# Exercise 43: Writing Multiple Lines
# Write the names "Ali", "Bala", "Cindy" each on a new line into names.txt.
# Expected Content (names.txt):
# Ali
# Bala
# Cindy




