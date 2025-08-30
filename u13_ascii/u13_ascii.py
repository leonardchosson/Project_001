
###################################################
# Part 1: Learning Exercises

# Exercise 1: Absolute Value of a Difference
# Find the absolute difference between two numbers.
# Example: Temperatures of two cities.

temp1 = 30
temp2 = 56

difference = temp1 - temp2
# print(abs(difference))




# #------------------------------------------------------------
# # Exercise 2: Convert Character to ASCII
# # Convert a character to its ASCII code and back again.
# abs()
# ord()
# chr()
# letter = "H"
# ord(letter)
# chr(letter)
# # find ordinal value (decimal value) from the ascii
# ordH = ord(letter) # ordinal
# print(ordH) # retrieves the ordinal number of H from ascii table

# letterH = chr(72) # character
# print(letterH)






# #------------------------------------------------------------
# # Exercise 3: Generating a Random Uppercase Letter
# # Generate a random uppercase letter using ASCII values.
import random
# randomnum = random.randint(65,90)
# letter = chr(randomnum)
# print(letter)

# count = 0
# letters = ""
# while count<8:
#     num = random.randint(65,90)
#     letter = chr(num)
#     letters += letter
#     count += 1 
# print(letters)

# #------------------------------------------------------------
# # Exercise 4: Generate ASCII Symbols
# # Generate a random special character from ASCII values.
# import random
# num = random.randint(33,47)
# print(chr(num))



# generate a password with 8 random special characters
# count = 0
# letters = ""
# while count<8:
#     num = random.randint(33,47)
#     letter = chr(num)
#     letters += letter
#     count += 1 
# print(letters)


# #------------------------------------------------------------

import random
### BONUS
# Generate a password containing the following
# 3 upper case letters
# 3 lower case letters
# 3 special characters
# 3 numbers
# '''33-47, 48-57, 65-90, 97-122'''
# password = ""
# for i in range(3):
#     num1 = random.randint(33,47)
#     password+=chr(num1)
# for i in range(3):
#     num2 = random.randint(48,57)
#     password+=chr(num2)
# for i in range(3):
#     num3 = random.randint(65,90)
#     password+=chr(num3)
# for i in range(3):
#     num4 = random.randint(97,122)
#     password+=chr(num4)
    
# temp = list(password)
# random.shuffle(temp)
# newpass = ''.join(temp)
# print(newpass)
## BONUS BONUS: randomize the position
# message = "I LOVE PIZZA"
# newmessage = ''
# key = 6
# for i in message:
#     num = ord(i)
#     num +=key
#     newmessage += chr(num)
# print(newmessage)




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 6: Random Username Generator
# The format is:
# first 3 characters of first name
# first 3 character of last name
# plus 3 printable characters from ASCII
# Scenario: Generate a random 9-character username using uppercase letters and digits.
import random
namey = ''
firstname = input("What is your first name?")
secondname = input("What is your last name?")
namey+=str(firstname[:3])
namey+=str(secondname[:3])
for i in range(3):
    num = random.randint(32,126)
    namey+=chr(num)
print(namey)
# namey+=


#