##############################################################
### ASCII ord() and chr() for password generation
##############################################################

# #Generate a Simple Password
# # Write a Python program that generates a random password of a given length 
#     using ASCII printable characters.
# # Example input: length = 8
# # Expected output: A random password of 8 characters, e.g., 'aB3#xG2!'
# # HINT: ASCII printable characters range from 33 to 126

# Sample solution 

# import random

# length = 8
# password = ""
# for i in range(length):
#     char = chr(random.randint(33, 126))  
#     password += char
# print(f"Generated password: {password}")


###########################################################
# Generate a Password with Specific Character Types
# Scenario 1: Corporate Password Policy - Basic Compliance
# One of your clients, a fintech company, has implemented a basic password policy. 
# All system-generated passwords must:
# - Be of a specific length
# - Include at least 1 uppercase letter, 1 lowercase letter, and 1 digit

# Your task: Write a Python program to generate such a password.
# Example: input = 8 → output = 'aB3xG2#1'

# HINT: Use ASCII:
# - Uppercase letters: 65-90
# - Lowercase letters: 97-122
# - Digits: 48-57


# Write and test your code here
# import random
# password = ''
# length = int(input("How lond will the password be?"))

# for i in range(length-3):
#     letter = chr(random.randint(33,126))
#     password+=letter
# UPletter = chr(random.randint(65,90))
# lowletter = chr(random.randint(97,122))
# digit = chr(random.randint(48,57))
# password = password+UPletter+lowletter+digit
# print(password)
###########################################################
# Exclude Specific Characters in Password
#  Scenario 2: Readability-Enhanced Password Generator
# A logistics firm found that users often confuse similar-looking characters 
# (like 'l', '1', 'I', 'O', and '0') when reading out passwords over the phone.
# To improve usability, you're tasked to generate passwords that:
# - Are of a specific length
# - Exclude these confusing characters: 'l', '1', 'I', 'O', '0'
# Example: input = 8, exclude = 'l1IO0' → output = 'aB3xG#2!'
# Hint: Any character in 33-126 except ASCII codes 48, 49, 73, 79, 108
# Write and test your code here

# import random
# password = ''
# length = int(input("How lond will the password be?"))
# confusing_chars = ['l', '1', 'I', 'O', '0']
# while len(password) < length:
#     letter = chr(random.randint(33, 126))
#     if letter not in confusing_chars:
#         password += letter
# print(password)





###########################################################
# Password with Special Characters
# Scenario 3: System Admin Access Passwords
# System administrators require strong passwords with at least 2 special characters 
# to prevent brute-force attacks.
# Your task:
# - Generate a password of a given length
# - Ensure it includes at least two special characters
#   (characters that are neither letters nor digits, e.g., '@', '#', '$', '%', etc.)
# Example: input = 8 → output = 'aB3@xG#2'
# Hint: ASCII 33-47: ! " # $ % & ' ( ) * + , - . /
# Write and test your code here
# import random
# password = ''
# length = int(input("How lond will the password be?"))
# for i in range(length-2):
#     letter = chr(random.randint(33,126))
#     password+=letter
# for i in range(2):
#     specialchars = chr(random.randint(33,47))
#     password+=specialchars
# print(password)


###########################################################
# import random
# password_chars = []
# password = ''
# length = int(input("What is the length of the password? "))
# while length < 8:
#     length = int(input("Password must be at least 8 characters. Enter again: "))
# org_length = length
# for i in range(2):
#     password_chars.append(chr(random.randint(65,90)))
# length -= 2
# for i in range(2):
#     password_chars.append(chr(random.randint(97,122)))
# length -= 2
# for i in range(2):
#     password_chars.append(chr(random.randint(48,57)))
# length -= 2
# for i in range(2):
#     specialchar = random.choice([
#         chr(random.randint(33,47)),
#         chr(random.randint(58,64)),
#         chr(random.randint(91,96)),
#         chr(random.randint(123,126))
#     ])
#     password_chars.append(specialchar)
# length -= 2
# for i in range(length):
#     password_chars.append(chr(random.randint(33,126)))
# random.shuffle(password_chars)
# for i in range(org_length):
#     password += password_chars[i]
# print(f"Generated password: {password}")

# 33-47, 58-64, 91-96, 123-126
###########################################################


###########################################################
# Calculate Checksums for a List of Network Messages
#
# A computer needs to send several text messages across a network.
# Before each message is sent, the computer calculates a checksum.
#
# The checksum is calculated using this algorithm:
# 1. Convert each character in the message into its ASCII value.
# 2. Add up all the ASCII values.
# 3. Calculate the total modulo 256.
#
# Checksum = total ASCII value % 256
#
# Your task:
# Write a Python program that:
# - Uses the given list of 5 messages
# - Loops through each message in the list
# - Calculates the checksum of each message
# - Outputs each message and its checksum
#
# Expected output:
#
# The server is ready -> 9
# Send the file now -> 31
# Login request accepted -> 123
# Data packet received -> 121
# Connection closed -> 170
#
# HINT:
# - Spaces are also characters and must be included in the checksum.
# - Use ord(character) to get the ASCII value of a character.
# - Use % 256 to calculate the checksum.
#
# Write and test your code here
messages = [
    "The server is ready",
    "Send the file now",
    "Login request accepted",
    "Data packet received",
    "Connection closed"
]
for msg in messages:
    total = 0
    for ch in msg:
        total += ord(ch)
    checksum = total % 256
    print(f"{msg} -> {checksum}")