# Task 3

# The following program should identify if a student receives either a gold, silver or bronze award for joint achievement in Computing and Mathematics. Each student has taken a test in Computing and a test in Mathematics. The program uses the rules:

# ·       A student receives a gold award for a test score of 100 or greater in both Computing and Mathematics.

# ·       A student receives a silver award for a test score of 100 or greated in Computing or Mathematics. They also need a combined Computing and Mathematics score of 180 or greater.

# ·       A student receives a bronze award for a test score of 75 or greater in both Computing and Mathematics.

# The test scores are whole numbers only. The program finishes when there are no more student test scores to be input. The award a student receives is output after the test scores for that student are input.

# There are several syntax and logic errors in the program.


students = False
while students == False:  # True to flase
    comp = int(input("Enter the Computing test score "))  # int()
    math = int(input("Enter the Mathematics test score ")) # missing quotation
    joint_score = comp + math # comp to math
    print(joint_score)
    if comp >= 100 and math >= 100:  # > to >=
        print("Student is awarded a gold award")
    elif (comp >= 100 or math >= 100 ) and joint_score >= 180: # "or" and "and" are switched
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
    if more_scores == 'N': #Morescores instead of morescores
        students = True 
    else:
        students = False  #True to false

# Open the file AWARDS.py

# Save the file as MYAWARDS_<your name>_<centre number>_<index number>.py

# 9 Identify and correct the errors in the program so that it works according to the rules given.

# Save your program.

# [10]