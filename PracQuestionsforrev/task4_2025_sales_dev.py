#3:10 start   end 3:50          40min spent
# Task 5

# A company is creating a system to calculate, record and 
# output different information relating to customer sales.

# All code should have appropriate comments and all identifiers 
# should be appropriately named. [4]

# You can assume that all costs will be valid and in dollars.

#========================================================
# Task 5.1
# Write a function total_cost() that calculates the total cost of a sale by:
# •	taking cost as a parameter
# •	calculating the total cost by adding 9% for tax purposes
# •	returning the total cost
# Save your program.
# [3]
# -------------------------------------------------

# Task 5.1

def total_cost(cost):
    total_cost = cost+9/100*cost  #add 9% GST
    return total_cost


#testing code
# print(total_cost(10))







# -------------------------------------------------


#========================================================
# Task 5.2
# Copy and paste your program from sub-task 5.1.
# A discount may be applied to a customer’s purchase.

# Extend the program by writing a function discount() that:
# •	takes cost as a parameter

# •	deducts a discount of 5% from the total cost if the 
#     total cost is between $50 (inclusive) and $100 (exclusive) 

# •	deducts a discount of 10% from the total cost if the 
#     total cost is $100 or greater 
# •	returns the total cost with or without a discount as appropriate 

# Your function must use the function total_cost() to 
# calculate the total cost for the sale.

# Save your program.
# [4]

# -------------------------------------------------
# Task 5.2

# def total_cost(cost):
#     total_cost = cost+9/100*cost  #add 9% GST
#     return total_cost

# def discount(cost):
#     total = total_cost(cost)
#     print(total)
#     total = float(total)
#     if total>=50 and total<100:            #discount scenario 1
#         total = total-5/100*total
#     elif total>=100:                        # discount scenario 2
#         total = total-5/100*total
#     total = round(total,2)
#     return total

#testing code
# print(discount(50))

# ------------------------------------------------


#========================================================
# Task 5.3
# Copy and paste your program from sub-task 5.2.
# A customer receives reward points on a purchase.
# Extend your program by writing another function reward_points() that:

# •	takes the total cost with any discount applied as a parameter

# •	calculates the number of reward points received for the purchase. 
#   A customer receives 3 reward points for each whole dollar ($) spent 

# •	returns the number of reward points received. 
# Save your program.
# [3]

# -------------------------------------------------
# Task 5.3

# def total_cost(cost):
#     total_cost = cost+9/100*cost  #add 9% GST
#     return total_cost

# def discount(cost):
#     total = total_cost(cost)
#     print(total)
#     total = float(total)
#     if total>=50 and total<=100:            #discount scenario 1
#         total = total-5/100*total
#     elif total>=100:                        # discount scenario 2
#         total = total-5/100*total
#     total = round(total,2)
#     return total

# def reward_points(totalcost):
#     points = 0
#     while totalcost>=1:   #only adds 3 points if a full dollar is spent
#         totalcost-=1
#         points +=3
#     return points

#testing code
# print(reward_points(4))












# -------------------------------------------------



#========================================================
# Task 5.4
# Copy and paste your program from sub-task 5.3.
# A customer may receive a voucher code that can be used for a future purchase. 
# Extend your program by writing a function voucher() that:

# •	takes the total cost with any discount applied and the customer’s 
#   first name as parameters

# •	creates a voucher code that is the first three letters of the customer’s name 
#   then the string "05PERCENT", if the total cost is between $25 (exclusive) and $50 (inclusive)

# •	creates a voucher code that is the first three letters of the customer’s name 
#   then the string "10PERCENT", if the total cost is greater than $50

# •	returns the voucher code or None as appropriate.
# Save your program.
# [3]

# -------------------------------------------------
# Task 5.4

# def total_cost(cost):
#     total_cost = cost+9/100*cost  #add 9% GST
#     return total_cost

# def discount(cost):
#     total = total_cost(cost)
#     total = float(total)
#     if total>=50 and total<100:            #discount scenario 1
#         total = total-5/100*total
#     elif total>=100:                        # discount scenario 2
#         total = total-5/100*total
#     total = round(total,2)
#     return total

# def reward_points(totalcost):
#     points = 0
#     while totalcost>=1:   #only adds 3 points if a full dollar is spent
#         totalcost-=1
#         points +=3
#     return points
# print(reward_points(4))

# def voucher(totalcost,first_name):
#     total = totalcost
#     voucher_code = ""
#     first_3 = first_name[:3]   #get the first 3 letters
#     if total>25 and total<50:     #value check
#         voucher_code = first_3+"05PERCENT"
#     elif total>50:                    #value check
#         voucher_code = first_3+"10PERCENT"
#     return(voucher_code)

# test code
# print(voucher(51,"leonrad"))  




# -------------------------------------------------



#========================================================
# Task 5.5
# Copy and paste your program from sub-task 5.4.
# The company wants an interface for the system.

# Extend your program to create an interface that:
#   •	takes the first name of the customer as input

#   •	takes the cost of the sale as input

#   •	outputs a receipt for the customer, using the correct functions, that shows:
#       o	the title "Receipt" 
#       o	the total cost of the sale (to 2 decimal places)
#       o	the discounted cost of the sale (to 2 decimal places)
#       o	the reward points received
#       o	the voucher code created. If no voucher code is created the text 
#           "You need to spend over $25 for a voucher code." should be output

#   •	writes the voucher code that is created (if any) to the file vouchercode.txt 

# Suitable input and output messages must be used.
# Save your JupyterLab notebook for Task 5.
# [8]

# -------------------------------------------------
# Task 5.5

def total_cost(cost):
    total_cost = cost+9/100*cost  #add 9% GST
    return total_cost

def discount(cost):
    total = total_cost(cost)
    total = float(total)

    if total>=50 and total<=100:            #discount scenario 1
        total = total- ((5/100) * total)
    elif total>=100:                        # discount scenario 2
        total = total-5/100*total
    total = round(total,2)
    return total

def reward_points(totalcost):
    points = 0
    while totalcost>=1:   #only adds 3 points if a full dollar is spent
        totalcost-=1
        points +=3
    return points

#testing
# print(reward_points(4))

def voucher(totalcost,first_name):
    total = totalcost
    voucher_code = None # 
    first_3 = first_name[:3] #value check
    if total>25 and total<50:
        voucher_code = first_3+"05PERCENT"
    elif total>50:           # value check
        voucher_code = first_3+"10PERCENT"
    return(voucher_code)

name = input("Enter your first name: ")
cost = float(input("How much was the cost of the sale? "))

print("Receipt")
total = round(total_cost(cost),2)
print(f"The total cost of the sale is ${total}")

discounted_cost = discount(total)
print(f"The total discounted cost of the sale is ${discounted_cost}")

print(f"The amount of points recived is {reward_points(discounted_cost)}")

code = voucher(discounted_cost,name)


# if discounted_cost>25:
if code != None:
    # voucher_name = voucher(discounted_cost,name)
    print(f"Your voucher code is {code}.")
    with open("vouchercode.txt","w") as f:
        f.write(code)
else:
    print("You need to spend over $25 for a voucher code.")




# -------------------------------------------------
