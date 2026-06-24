import random
questions = 10
answer_list = []  #missing =
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions):   #questions not questions -1
    num1 = (random.randint(1,50))
    num2 = (random.randint(1,50))
    answer = num1 + num2       #ans not userans
    print(answer)
    print("What is", num1, "+", num2, "?")
    user_answer = input()
    if user_answer == answer:
        if num1 > 25 or num2 > 25:
            total_mark = total_mark + 2
            answer_list.append("Correct")   #.append() not +
        else:
            total_mark = total_mark + 1
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) - 1   #error
for i in range(list_length):
    if answer_list[x] == "Correct":
        correct = correct - 1
if correct == 1:  #correct not message
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark,"and you had", correct, "correct", message)