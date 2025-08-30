# dict = {"yes":1,"ok":2, "alright":3}
# for i, value in dict.items():
#     print(i, value)
'''A class has 15 students. The following program allows a teacher to input the favourite hobby
of each student in the class.
num_students = 15
for x in range(num_students):
hobby = input("What is the student's favorite hobby? ")
Open the file HOBBY.py.
Save the file as MYHOBBY_<your name>_<centre number>_<index number>

1 Edit the program to use a conditional loop that repeats until the teacher does not want
to enter any more hobbies. You may choose to modify the for-loop into a while loop to
suit your algorithm.
Suitable input messages must be used.
Save your program. [3]
2 Edit your program to convert each student’s hobby to lower case and then store it in a
list.
Save your program. [2]
3 Edit your program to display the number of students that have a specific favourite hobby.
The program must:
• ask the teacher to input a hobby to search for in the list
• output the hobby and the number of students who have that specific hobby as their
favorite hobby.
Suitable input and output messages must be used.
Save your program. [5]'''
# hobbies = []
# while True:
#     hobby = input("What is the student's favorite hobby? (type 'end' to finish): ").lower().strip()
#     if hobby == "end":
#         break
#     hobbies.append(hobby)

# print("\nAll hobbies recorded.")
# choice = input("Enter a hobby to search for: ").lower().strip()

# # Count how many times the hobby appears
# count = hobbies.count(choice)

# print(f"\nThe hobby '{choice}' is the favorite of {count} student(s).")
'''A program allows the user to input the cost of item and amount be paid, and calculates the
change returned in as fewest number of coins possible. The program also returns a message
if the amount to be paid is lower than the cost of the item.
cost = int(input("Enter cost of item (in cents): "))
paid = int(input("Enter the amount paid (in cents): ")

Open the file CHANGE.py.
Save the file as MYCHANGE_<your name>_<centre number>_<index number>'''


name = "Bala"
money = 2.85
pizza_price = 20.24
slice_price = pizza_price / 8
discount_price = int(slice_price)
can_buy = money >= discount_price
output = name + ' can buy slice at price $' + str(discount_price)
output += ': ' + str(can_buy)
print(output)