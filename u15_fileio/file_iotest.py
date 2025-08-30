# # A text file shapes.txt stores a list of shapes 
# # with a comma between each value.  

# # The current contents of shapes.txt are: 
# # star,sphere,square,triangle 

# # A text file colours.txt stores a list of 
# # colours with a comma between each value.  

# # The current contents of colours.txt are: 
# # red,yellow,green,blue 

# # A program reads the data from each file and 
# # creates a dictionary of the values so that each shape
# #  has an associated colour. 
# # The first value in each file will be joined, for example, star and red. 

# # The data is stored in a global dictionary with the identifier data_store

# #########################################
# # Task A 6 - marks
# # The function read_values() reads the data from both files 
# # and stores the data in the global dictionary data_stored.  

# # The data from the shapes.txt file is used as the key 
# # and the data from the colours.txt file is used as the value. 

# # The function needs to work for files of any length. 
# # The files will always have the same number of data values. 

# # Write program code for the function read_values(). 
# #########################################
# # Write code for Task A here
# data_stored = {}

# def read_values():
#     with open("shapes.txt", "r") as shapesf:
#         Shapestring = shapesf.read()
#     with open("colours.txt", "r") as colourf:
#         Colourstring = colourf.read()
#     Shapelist = Shapestring.split(",")
#     Colorlist = Colourstring.split(",")
#     for i in range(len(Shapelist)):
#         data_stored[Shapelist[i]] = Colorlist[i]
#     # ['star','spheere', ..]
#     # ['red', 'yellow'...]

#     # # loop through using the index
#     # for i in range(len(Shapelist)):
#     #     currentshape = Shapelist[i]
#     #     currentcolor = Colorlist[i]

#     #     # put into dictionary
#     #     data_stored[currentshape] = currentcolor

#     # star,sphere,square,triangle
# # red,yellow,green,blue
    






# #########################################
# # Task B -  4 marks
# # The function output_result() asks the user to enter a shape 
# # until the shape entered is found in the dictionary. 
# # The colour for that shape is printed out. 

# # Write program code for the function output_result(). 
# #########################################
# # Write code for Task B here
# def output_result():
#     while True:
#         shape = input("Enter a shape: ")
#         if shape in data_stored:
#             print(data_stored[shape])
#             break
#         else:
#             print("Shape not found, try again.")








bags_rice = 10
upper_num = 0
upper_bound = 5.1
lower_num =0
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        upper_num +=1
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")
        lower_num +=1
    if bag_weight <= upper_bound and bag_weight >= lower_bound:
        print("The bag of rice is the correct weight")
print(f"There were {lower_num} underweight bags ")
print(f"There were {upper_num} underweight bags ")
# Open the file RICEBAGS.py

# Save the file as MYBAGS_<your name>_<center number>_<index number>.py

 

# 7       Edit the program so that it:

# a.       Accepts the weights for only 10 bags of rice.
# [1]

# b.       Prints out the message “The bag of rice is the correct weight” when a weight entered is between 4.9kg and 5.1 kg inclusive.
# [2]

# c.       Prints out the number of bags of rice that were underweight, as well as the number that were overweight, after the weights of all the bags have been entered.
# [5]

# Save your program.


# 8       Save your program as VARBAGS_<your name>_<center number>_<index number>.py

# Edit your program so that it works for any number of bags of rice.

# bags_rice = input("Enter the number of bags of rice that will be entered")
# upper_num = 0
# upper_bound = 5.1
# lower_num =0
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#         upper_num +=1
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")
#         lower_num +=1
#     if bag_weight <= upper_bound and bag_weight >= lower_bound:
#         print("The bag of rice is the correct weight")
# print(f"There were {lower_num} underweight bags ")
# print(f"There were {upper_num} underweight bags ")
# Save your program.

# [2]

# RICEBAGS.py RICEBAGS.py1 April 2025, 10:49 AM


flagg = True
list_name_totals = []
counter = 1
total = 0

while flagg:
    name = input("Please enter the Player's name: ")
    length_string = name.len()
    name = name.lower()
    print("You are player " + str(count))

    for x in range(length_string - 1):
        char = name[x]
        value = num(char)
        total = value + value

    list_name_totals.append(value) 
    print("Your total is " + str(total))

    more = input("Would you like to enter another player's name? Enter Yes or No. ")
    if more == "yes":
        flagg = True
    else:
        count += 1

    highest = ceil(list_name_totals)
    for x in range(list_name_totals):
        if list_name_totals[x] == highest:
            position = x 

    print("The highest value is " + str(highest) + " and that is player " + str(position))