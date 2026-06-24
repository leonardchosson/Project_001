            # start: 2:41                  End:301     Ended 2:51
# """
# Task 2 2025
# Mock Question 1 - Temperature

# # The following program allows the entry of temperatures for a week.
# # The program checks if the temperature is within a normal range 
# # (24°C to 28°C inclusive).
# """
# days = 7
# normal_min = 24
# normal_max = 28
# for day in range(days):
#     temp = float(input("Enter the temperature for the day: "))
#     if temp > normal_max:
#         print("The temperature is too high")
#     if temp < normal_min:
#         print("The temperature is too low")

# For each of the sub-tasks, add a comment using the hash symbol 
# '#' at the beginning of your code to indicate the sub-task 
# that the program code belongs to. 

# Open the file TEMPERATURE.ipynb. Save the file as 
# MYTEMP_<your name><center number><index number>.ipynb

# # --------------------------------------
# Task 1.1 
# # --------------------------------------
# Edit the program so that it:
# Accepts temperatures for only 5 days.  [1 mark]

# Task 1.1

# days = 5
# normal_min = 24
# normal_max = 28
# for day in range(days):
#     temp = float(input("Enter the temperature for the day: "))
#     if temp > normal_max:
#         print("The temperature is too high")
#     if temp < normal_min:
#         print("The temperature is too low")






# # --------------------------------------
# Task 1.2
# # --------------------------------------
# Prints "The temperature is normal" when the temperature 
# is between 24°C and 28°C inclusive. 
# [2 marks]

# Task 1.2

# days = 5
# normal_min = 24
# normal_max = 28
# for day in range(days):
#     temp = float(input("Enter the temperature for the day: "))
#     if temp > normal_max:
#         print("The temperature is too high")
#     if temp < normal_min:
#         print("The temperature is too low")
#     if temp>= 24 and temp<= 28:
#         print("The temperature is normal.")








# # --------------------------------------
# Task 1.3
# # --------------------------------------
# Counts and prints the number of days with temperatures 
# too high and too low after all inputs. 
# [3 marks]
# Save your program.

    #Task 1.3


# days = 5
# normal_min = 24
# normal_max = 28
# counthot = 0
# countlow = 0
# for day in range(days):
#     temp = float(input("Enter the temperature for the day: "))
#     if temp > normal_max:
#         print("The temperature is too high")
#         counthot+=1
#     if temp < normal_min:
#         print("The temperature is too low")
#         countlow+=1
#     if temp>= 24 and temp<= 28:
#         print("The temperature is normal.")
# print(f"There were {counthot} days with high temperatures and {countlow} days with low temperatures")






# # --------------------------------------
# Task 1.4
# # --------------------------------------
# Save your program as VARTEMP_<your name><center number><index number>.py
# Edit your program to allow the user to enter any number of days. 
# Ensure that the input is a valid whole number 
# by performing input validation. The program should repeatedly 
# prompt the user until a valid number is entered. 
# Save your program. 
# [4 marks]

# Task 1.4
while True:
    days = input("Enter the amount of days of data going to be put in that is a whole number. ")
    try:
        int(days)
    except ValueError:
        days = input("Enter the amount of days of data going to be put in that is a whole number. ")
    else:
        days = int(days)
        break
normal_min = 24
normal_max = 28
counthot = 0
countlow = 0
for day in range(days):
    temp = float(input("Enter the temperature for the day: "))
    if temp > normal_max:
        print("The temperature is too high")
        counthot+=1
    if temp < normal_min:
        print("The temperature is too low")
        countlow+=1
    if temp>= 24 and temp<= 28:
        print("The temperature is normal.")
print(f"There were {counthot} days with high temperatures and {countlow} days with low temperatures")

