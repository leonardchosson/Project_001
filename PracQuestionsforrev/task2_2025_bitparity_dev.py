# G3 Computing Prelim
# Python Development Question – Parity Bit Generation and Validation [25 marks]
# A parity bit is a simple form of error detection used in networking. 
#   An extra bit, called the parity bit, is added to a binary string.

# In this question:
# •	A 7-bit binary string contains data bits only.
# •	An 8-bit binary string contains 7 data bits followed by 1 parity bit.
# •	The rightmost bit of the 8-bit binary string is the parity bit.

# For EVEN parity, the total number of 1 bits in the 
#     8-bit binary string should be even.
# For ODD parity, the total number of 1 bits in the 
#     8-bit binary string should be odd.

# You will write a Python program that can:
# 1.	generate an 8-bit binary string from a 7-bit binary string 
#       by adding the correct parity bit, and
# 2.	validate whether an 8-bit binary string has the correct parity bit.

# The program should be developed using functions. 
# Each function should complete a specific part of the whole program. 
# The final main program should call these functions to complete the full program.

# Program quality [4]
# Your program must:
# •	use appropriate input and output messages,
# •	use meaningful variable and function names,
# •	include suitable comments to explain important parts of the algorithm.


# ________________________________________
# Task 1
# Write a function is_valid_binary_string(binary_str, required_length) 
#   that accepts two parameters: [3]
#   •	binary_str, which is the string to be checked,
#   •	required_length, which is the required number of characters.

# The function should return True if:
# •	binary_str has exactly required_length characters, and
# •	every character in binary_str is either "0" or "1".

# Otherwise, the function should return False.
#   For example:
#       is_valid_binary_string("1010101", 7)
#           should return True.
#       is_valid_binary_string("1010201", 7)
#           should return False.
# ________________________________________
# Code for Task 1

# def is_valid_binary_string(binary_str, required_length):
#     # Check length
#     if len(binary_str) != required_length:
#         return False
#     # Check each character
#     for char in binary_str:
#         if char not in ["0", "1"]:
#             return False
#     return True
#testings
# print(is_valid_binary_string("1010101",7))
# print(is_valid_binary_string("1010121",7))

# ________________________________________
# Task 2
# Write a function generate_parity_binary(data_bits, parity_type) 
#       that accepts two parameters: [6]
# •	data_bits, which is a valid 7-bit binary string,
# •	parity_type, which is either "EVEN" or "ODD".

# The function should:
#   •	count the number of "1" bits in data_bits,
#   •	determine the correct parity bit based on parity_type,
#   •	append the parity bit to the end of data_bits,
#   •	return the resulting 8-bit binary string.
#       For example:
#           generate_parity_binary("1010001", "EVEN")
#               should return:
#                   "10100011"
# This is because "1010001" has three 1 bits. 

# For EVEN parity, the parity bit must be "1" so that the total 
# number of 1 bits becomes even.
# ________________________________________
# Code for Task 2

def is_valid_binary_string(binary_str, required_length):
    # Check length
    if len(binary_str) != required_length:
        return False
    # Check each character
    for char in binary_str:
        if char not in ["0", "1"]:
            return False
    return True

def generate_parity_binary(data_bits, parity_type):
    counter1 = 0
    for bin in data_bits:
        if bin == "1":
            counter1+=1
    if parity_type == "EVEN":
        if counter1%2==0:
            return data_bits +"0"
        else:
            return data_bits + "1"
    elif parity_type == "ODD":
        if counter1 %2 == 1:
            return data_bits+"0"
    else:
        return data_bits +"1"
        


# def generate_parity_binary(data_bits, parity_type):
#     # ODD/ EVEN
#     count1 = 0
#     for char in data_bits:
#         if char == "1":
#             count1 += 1

#     if parity_type == "EVEN":
#         if count1 % 2 == 0:
#             return data_bits + "0"
#         else:
#             return data_bits + "1"
#     elif parity_type == "ODD":
#         if count1 % 2 == 1:
#             return data_bits + "0"
#         else:
#             return data_bits + "1"

# print(generate_parity_binary("1010001", "EVEN"))
# print(generate_parity_binary("1010001", "ODD"))



# ________________________________________
# Task 3
# Write a function validate_parity(binary_str, parity_type) 
#       that accepts two parameters: [4]
#       •	binary_str, which is a valid 8-bit binary string,
#       •	parity_type, which is either "EVEN" or "ODD".
# The function should:
#   •	count the total number of "1" bits in the entire 8-bit binary string,
#   •	check whether the total number of "1" bits is correct for the 
#           selected parity type,
#   •	return True if the parity is correct,
#   •	return False otherwise.

#        For example:
#           validate_parity("10100011", "EVEN")
#               should return True.
#           validate_parity("10100010", "EVEN")
#               should return False.
# ________________________________________
# Code for Task 3







# ________________________________________
# Task 4
# Write the main program. [8]
# The main program should:
#   1.	Ask the user to enter a parity mode.

#   2.	Keep asking until the user enters either "EVEN" or "ODD".
#       o	The input should be accepted regardless of case.
#       o	The validated parity mode should be stored in uppercase.

#   3.	Ask the user to choose one of the following options:
#       1. Generate an 8-bit binary string
#       2. Validate an 8-bit binary string

#   4.	If the user chooses option 1:
#       o	ask the user to enter a 7-bit binary string,
#       o	call is_valid_binary_string(data_bits, 7) to check whether 
#               the input is valid,
#       o	keep asking until a valid 7-bit binary string is entered,
#       o	call generate_parity_binary(data_bits, parity_type),
#       o	display the generated 8-bit binary string clearly.

#   5.	If the user chooses option 2:
#       o	ask the user to enter an 8-bit binary string,
#       o	call is_valid_binary_string(binary_str, 8) to check whether 
#               the input is valid,
#       o	keep asking until a valid 8-bit binary string is entered,
#       o	call validate_parity(binary_str, parity_type),
#       o	display clearly whether the parity is valid or invalid.
# ________________________________________
# Code for Task 4


