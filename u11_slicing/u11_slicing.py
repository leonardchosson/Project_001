# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Simple List Slicing
# # Write a program to extract the first 3 elements from a list.
# numbers = [10, 20, 30, 40, 50]
# sliced_numbers = numbers[:3]  # Extract elements from index 0 to 2
# print("First 3 elements: {}".format(sliced_numbers))




# #------------------------------------------------------------
# # Exercise 2: Negative Indexing
# # Write a program to extract the last 2 elements from a list 
# # using negative indexing.
# numbers = [10, 20, 30, 40, 50]
# last_two = numbers[-2:]  # Extract last 2 elements
# print("Last 2 elements: {}".format(last_two))




# #------------------------------------------------------------
# # Exercise 3: Skipping Elements in a List
# # Write a program to extract every other element from a list.
# numbers = [10, 20, 30, 40, 50, 60]
# skipped_numbers = numbers[::2]  # Skip every second element
# print("Every other element: {}".format(skipped_numbers))




# #------------------------------------------------------------
# # Exercise 4: Reversing a List Using Slicing
# # Write a program to reverse a list using slicing.
# numbers = [10, 20, 30, 40, 50]
# reversed_numbers = numbers[::-1]  # Reverse the list
# print("Reversed list: {}".format(reversed_numbers))




# #------------------------------------------------------------
# # Exercise 5: Simple String Slicing
# # Write a program to extract the first 5 characters from a string.
# text = "Hello, world!"
# sliced_text = text[:5]  # Extract characters from index 0 to 4
# print("First 5 characters: {}".format(sliced_text))




# #------------------------------------------------------------
# # Exercise 6: String Slicing with Steps
# # Write a program to extract every second character from a string.
# text = "abcdefg"
# skipped_chars = text[::2]  # Skip every second character
# print("Every second character: {}".format(skipped_chars))




#------------------------------------------------------------
# Exercise 1: Extracting Initials from a Name
# Scenario: A company wants to display initials for employees on ID cards.
# Given a full name, extract the initials.

# Example:
# Input: "John Michael Smith"
# Output: "J.M.S"

# Input: "Alice Bob"
# Output: "A.B"

name = "John Michael Smith"

print(name)





###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
# numbers = [10, 20, 30, 40, 50, 60, 70]
# length = len(numbers) // 2
# first = length - 1
# second = length + 1
# print(numbers[first:second+1])



#------------------------------------------------------------

# Exercise 8: Checking Palindrome in a String
# Scenario: Determine if a string is a palindrome (reads the same 
# backward as forward).
# word = input("Enter a word: ")
# if word[::-1] == word:
#     print("It is a pallindrom")
# else:
#     print("It is not a pallindrom")




#------------------------------------------------------------

# Exercise 9: Reversing Words in a Sentence
# Scenario: Reverse the words in a sentence manually.
### learn to fun is 
sentence = "Python is fun to learn."
sentences = sentence.split()
sentence = sentences[::-1]
print(sentence)
sentences = ''
for i in sentence:
    sentences += sentence[i]
print(sentence)





#------------------------------------------------------------
# Exercise 10: Validating a Substring
# Scenario: Check if a string contains only alphabets using slicing.
text = "Hello123"
# for i in text:
#     if text.isalpha() == True:
        



#-----------------------------------------------------------