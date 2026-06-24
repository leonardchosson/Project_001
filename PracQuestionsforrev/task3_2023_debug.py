#start: 3:17      End: 3:37
# 2023 – Task 3 [10]
# A mathematics program shown on the next page creates 10 questions.
# Each question is created by generating two random integers 
# between 1 and 50 inclusive and adding them.

# The program:
# •	outputs the questions
# •	allows the user to input their answer to each question
# •	outputs the user's total mark and the number of correct answers
# •	alters the output based on whether 1 or multiple correct answers are given.

# If both random integers are greater than 25, the user gets 2 marks 
# for a correct answer, otherwise, the user gets 1 mark for a correct answer.
    
# If the user enters a correct answer:
# •	the total mark is incremented by the correct amount
# •	the text "Correct" is stored in a list, otherwise, the text "Incorrect" is stored in the list.
# When all questions have been answered, the list is searched to count how many times "Correct" is stored.

import random
questions = 10
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions):    #without -1 because with it, it will ask the questions 9 times only
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    print(num1 +num2)
    print("What is", num1, "+", num2, "?")
    user_answer = input()
    if user_answer == num1+num2:                #1. answer not defined, calculate here for num1 + num2 not ans 
        if num1 > 25 and num2 > 25:        #and not or
            total_mark = total_mark + 2
            answer_list = answer_list + ["Correct"]
            print(answer_list)
        else:
            total_mark = total_mark + 1
            print(answer_list)
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list)-1   #            put the 1 outside
for i in range(list_length):
    if answer_list[i] == "Correct":         #                         i not x
        print(i)
        correct = correct + 1               # + not -
if correct  == 1:               # correct not message
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)

# Open the file MATHS.py
# Save the file asMYMATHS_2023___.py

# 1.	Identify and correct the errors in the program so that it works 
# according to the requirements given

# Save your program.
# [10 marks]
