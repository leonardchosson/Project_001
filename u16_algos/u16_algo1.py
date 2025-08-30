########################################################
# Question 3:
# The student council organised a charity fundraising event. 
# The amount collected from each class is stored in the dictionary below. 
# Identify the class that raised the highest and lowest amounts. 
# Print out the class names and their respective contribution amounts.
########################################################
# donations = {
#     'Class 1A': 320, 'Class 1B': 480, 'Class 1C': 290, 'Class 1D': 375,
#     'Class 1G': 450, 'Class 1H': 530, 'Class 2C': 470, 'Class 3D': 310,
#     'Class 4E': 415, 'Class 5F': 390
# }
# # Answer for Question 3 here
# maxim = 0
# lowest = 10000000000
# for i in donations:
#     amount = (donations[i])
#     if amount > maxim:
#         maxim = amount
#     if amount < lowest:
#         lowest = amount
# for e in donations:
#     if donations[e] == maxim:
#         print("The class who donated the most amount of money is", e,"Amount: $",maxim)
#     if donations[e] == lowest:
#         print("The class who donated the least amount of money is", e,"Amount: $", lowest)















conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "GB": 1000**3,
    "TB": 1000**4,
    "KiB": 1024,
    "MiB": 1024**2,
    "GiB": 1024**3,
    "TiB": 1024**4,
    "PiB": 1024**5,
}

# Extend the conversion_factors dictionary to include the following units:

# SI units: "GB", "TB", "PB"
# Binary units: "GiB", "TiB", "PiB"
# Use the appropriate powers of 1000 for SI units and 1024 for binary units.

# Task 4.2 – Validation Function [4 marks]

# Write a function named is_valid_unit(unit) that:

# Takes in a string unit
# Returns True if the unit is a valid key in the conversion_factors dictionary
# Returns False otherwise
# This function will be used to check whether the user has entered a supported unit.

# Task 4.3 – Conversion Function [7 marks]

# Write a function named convert_storage(value, from_unit, to_unit) that:

# Takes in three parameters:
# value (a numeric value to convert)
# from_unit (the current unit)
# to_unit (the target unit)
# Converts the value using the following steps:
# 1.                      Multiply the value by the conversion factor of the source unit to get the number of bytes

# 2.                      Divide the number of bytes by the conversion factor of the target unit to get the result
def convert_storage(value, from_unit, to_unit):
    num_bytes = value*(conversion_factors[from_unit ])
    output = num_bytes/conversion_factors[to_unit]
print(convert_storage(1000, "TB", "PiB"))
# Returns the final result as a float
# Use the conversion_factors dictionary for all conversions.
# Do not perform any user input or output in this function.
# Do not use if or elif statements to check unit names.

# This function must correctly handle:

# Conversion from a larger unit to a smaller unit (e.g. GB → MB)
# Conversion from a smaller unit to a larger unit (e.g. KiB → GiB)
# Task 4.4 – User Interaction [8 marks]

# Write the main program that:

# Repeatedly prompts the user to input:
# A numeric value
# A source unit
# A target unit
# Validates that:
# The numeric value is positive.
# Both units are supported using the is_valid_unit() function
# Calls the convert_storage() function to perform the conversion
# Displays the result to 4 decimal places, e.g.:
# 10 MB is approximately 9.5367 MiB
# Asks the user whether they want to convert another value
# If the user enters "yes", repeat the process
# If the user enters "no", end the program
# Task 4.5 – Code Quality [4 marks]

# Ensure that your code:

# Uses meaningful and consistent variable and function names
# Is structured using appropriate function decomposition
# Includes inline comments that explain important parts of the logic
conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "GB": 1000**3,
    "KiB": 1024,
    "MiB": 1024**2,
    "GiB": 1024**3,
    "TiB": 1024**4,
    "PiB": 1024**5
}

def is_valid_unit(unit):
    if unit in conversion_factors:
        return True
    else:
        return False

def convert_storage(value, from_unit, to_unit):
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

unit = ""
cont = True
num = -1

while cont == True:
    while num <= 0:
        num = int(input("Enter a numeric value"))
    print('Number accepted')
    while True:
        from_unit = input("Enter the source unit")
        if is_valid_unit(from_unit):
            print(from_unit, "is valid")
        else:
            print(from_unit, "is not valid, try again")
            continue
        to_unit = input("Enter the target unit")
        if is_valid_unit(to_unit):
            outputval = convert_storage(num, from_unit, to_unit)
            outputval = round(outputval, 4)
            print(f"{num} {from_unit} is {outputval} {to_unit}")
            break
        else:
            print(to_unit, "is not valid, try again")
    again = input("Do you want to convert another value? (yes/no): ").lower()
    if again == "no":
        cont = False
    else:
        num = -1