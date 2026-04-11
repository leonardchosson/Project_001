# 1. ⭐⭐ RESULTS
# Task 3
# The following program collates the names and scores of students in a class.

# The program validates that the score is from 0 to 100 inclusive, and also computes and outputs:

# number of scores entered
# number of students who score distinction (75 or more)
# number of students who failed (below 50)
# average score in the class
# The program allows a user to continue entering the names and scores until the user enters the letter 'N' when prompted.

# There are several syntax errors and logical errors in the program.


# name_list = []
# mark_list = []
# dist_list = []
# pass_list = []
# fail_list = []
# count = 1

# flag = True
# while flag == False:
#     name = input('Enter student's name: ')
#     name_list += [name]
#     while True:
#         mark = int(input('Enter score of student: '))
#         if mark >= 0 or mark <= 100:
#             break
#         else:
#             print('Invalid mark!')
#         mark_list += [mark]
#     count += 1
#     if mark > 75:
#         dist_list += [name]
#     elif mark >= 50:
#         pass_list += [name]
#     else:
#         fail_list += (name)
#     more = int(input('Would you like to enter another score, Y or N?: '))
#     if more == 'N':
#         flag = False
# average = round(max(mark_list)/len(mark_list), 2)
# num_dist = len(dist_list)
# num_fail = len(fail_list)
# print("You entered " + count + " scores.")
# print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
# print("Average score is " + str(average))







# 1. ⭐⭐ RESULTS
# Task 3
# The following program collates the names and scores of students in a class.

# The program validates that the score is from 0 to 100 inclusive, and also computes and outputs:

# number of scores entered
# number of students who score distinction (75 or more)
# number of students who failed (below 50)
# average score in the class
# The program allows a user to continue entering the names and scores until the user enters the letter 'N' when prompted.

# There are several syntax errors and logical errors in the program.


name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0     #count = 0 not 1

flag = True
while flag == True:  #flag must be True to run
    name = input("Enter student's name: ")  #Change the "'" to a "" as "Student's" has "'"
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100:   #and not or
            break
        else:
            print('Invalid mark!')
    mark_list += [mark]     # not in the indent
    count += 1
    if mark >= 75:      # >= not >
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name]     #[] not ()
    more = input('Would you like to enter another score, Y or N?: ') # should not convert to int()
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2)   #sum not max
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.")     #convert count into a string
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))