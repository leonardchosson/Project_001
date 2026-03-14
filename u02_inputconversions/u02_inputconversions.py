
# Task 2 
# In Singapore, electronic road pricing (ERP) is implemented 
# on various expressways to regulate traffic. 
# 
# Lately there has been a change in the ERP rates at 5 gantries across some expressways. 

# The following program calculates the change in rates of these 5 gantries. 

# for i in range(5): 
#     expressway = input("Enter name of gantry:") 
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 

# Your program code and output for each of Tasks 2 should be saved 
# in a single .ipynb file using JupyterLab. For example, your program 
# code and output for Task 2 should be saved as:
#  TASK2___.ipynb

#  Make sure that each of your .ipynb files shows the required output in JupyterLab.
# For each of the sub-tasks, add a comment using the hash symbol ‘#’ 
# at the beginning of your code to indicate the sub-task 
# that the program code belongs to. 

###########################################################
# 6. Edit the program so that: 
# a)	It works for any number of gantries. 
#       The program must display a suitable input message. [1] 
###########################################################
# Copy + Paste & Write your code here
# while True: 
#     expressway = input("Enter name of gantry:") 
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 
#     choice = input("Are there any more expressways you would like to add? (Y or N)")
#     if choice.upper() == "N":
#         break



###########################################################
# b)	The name of gantry is accepted if it is made up of only 
#       letters and is of a maximum length of 20. 
#       A suitable error message must be displayed and the program 
#       must loop until the name of the gantry is an input of a maximum of 20 letters. [4] 
###########################################################
# Copy + Paste & Write your code here
number_gantries = int(input("How many gantrees will be inputted?"))
for i in range(number_gantries): 
    while True:
        expressway = input("Enter name of gantry:")

        # if len(expressway) > 20:
        #     print("Expressway name cannot be more than 20.")
        # elif expressway.isalpha() == False:
        #     print("Expressway name can only contain letters.")
        # else:
        #     break

        if len(expressway) <=20 :
            if expressway.isalpha() == True:
                break
            else:
                print("The name of the expressway is only in letters")
        else:
            print("The name of the expressway must be less than or equals to 20")
            
    old = float(input("Enter old rate:")) 
    new = float(input("Enter new rate:")) 
    change = new - old 
    print("Change is",change) 




###########################################################
# c)	The name of each gantry for which the ERP rate has 
#       been increased is stored in a list and then displayed. [4] 
###########################################################
# Copy + Paste & Write your code here
increased_name = []
number_gantries = int(input("How many gantrees will be inputted?"))
for i in range(number_gantries): 
    while True:
        expressway = input("Enter name of gantry:")
        if len(expressway) <=20 :
            if expressway.isalpha() == True:
                break
            else:
                print("The name of the expressway is only in letters")
        else:
            print("The name of the expressway must be less than or equals to 20")
    old = float(input("Enter old rate:")) 
    new = float(input("Enter new rate:")) 
    change = new - old 
    if change>0:
        expressway.append()
    print("Change is",change) 


###########################################################
# d)	The total number of gantries which saw an increase 
#       in the ERP rate is displayed. [1] 
###########################################################
# Copy + Paste & Write your code here