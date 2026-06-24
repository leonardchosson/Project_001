#2:41 tart
# '''
# Task 4 - 2023 Paper - Development of Program
# Open the file SPLIT_SENTENCE.py. You will see the following function that 
# takes a string of words, passed as the parameter word_string, splits it 
# into individual words and stores these words in a list. 
# It returns the list of words. 

# You can assume the string does not contain punctuation marks.
# '''
def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence

# print(split_sentence("Hello I am Leonard"))
# '''
# # Task 4.1
# 10.	Save the program as CHECK_LIST_2023_<your name>_<centre number>_<index number>.py [7 marks]
# Extend the program by writing another function check_list() that searches 
# through the list of words to find a certain word. 

# If it finds the word in the list, it returns "Yes", otherwise it returns "No". 
# The variable word needs to be passed to the function. 
# The function you write must use the function split_sentence() already provided.
# Save your program.
# '''
# #---------------------------------------
# # Task 4.1 [7]
# #---------------------------------------
# # write your code here
def check_list(word,sentence):
    sentence_list = split_sentence(sentence)    #converting sting into a list fro presence check
    if word in sentence_list:
        return "Yes"
    else:
        return "No"

# print(check_list("i", "Hello I am Leonard"))









# '''
# # Task 4.2
# 11.	Save your program as REVERSE_2023_<your name>_<centre number>_<index number>.py [7 marks]
# Extend your program by writing another function reverse_sentence() 
# that reverses the words in the string and returns the whole string reversed, 
# with spaces between the words. 

# For example, 
# "the cat sat on the mat" would return: "mat the on sat cat the". 

# The function you write must use the function split_sentence() already provided. 
# You must not use the slice operator or the reverse function available in Python. 
# Your program does not need to consider any spaces before or after 
# the reversed sentence. Save your program.
# '''
# # write your code here

# #---------------------------------------
# # Task 4.2 [7]
# #---------------------------------------

def reverse_sentence(sentence):
    sentence_list = split_sentence(sentence)   #split the strin into a list
    reverse_sentence= "" #temporary variable
    for word in sentence_list:
        reverse_sentence = word+ " " + reverse_sentence  #concatonation program
    return reverse_sentence

# print(reverse_sentence("Hello I am Leonard"))




# '''
# # Task 4.3
# 12.	Save your program as FUNCTIONS_2023_<your name>_<centre number>_<index number>.py [6 marks]

# Extend your program by using the functions created such that it:
# •	allows the user to input a string of words (validation of this is not necessary)
# •	allows the user to input a word to search for in the string of words
# •	outputs the string of words, split into a list
# •	outputs the string of words, reversed
# •	outputs whether the word input is found in the string of words.
# Save your program.
# '''


# #---------------------------------------
# # Task 4.3 [6]
# #---------------------------------------


# •	allows the user to input a string of words (validation of this is not necessary)
wordstring = input("Enter a string of words ")
# •	allows the user to input a word to search for in the string of words
Wordsearch = input("Enter a word to search for ")
# •	outputs the string of words, split into a list
print(split_sentence(wordstring))
# •	outputs the string of words, reversed
print(reverse_sentence(wordstring))
# •	outputs whether the word input is found in the string of words.
# for i in split_sentence(wordstring):
#     if check_list(Wordsearch, wordstring) == "Yes":
#         check = True

check =  check_list(Wordsearch, wordstring)

if check == "Yes":
    print(f"{Wordsearch} is found in {wordstring}.")
else:
    print(f"{Wordsearch} is not found in {wordstring}.")







