
### EXAMPLE DICTIONARY
# A dictionary variable holds a key and value pair
example = {
  'key1': 'value1',
  'key2': 'value2',
  'key3': 'value3',
  'key4': 'value4'
}

'''
################ Define a dictionary ###############
Define a dictionary named menu which will store a food item and price of food

'hamburger' costs 10
'pizza' costs 18.5
'lasagne' costs 25.70
'fries' costs 5
'''
# write and test your code here 
food = {}
food["Hamburger"] = 10
food["Pizza"] = 18.5
food["Lasagna"] = 25.7
food["Fries"] = 5
'''
################ Retrieve values from a dictionary ###############
Print out the price of Lasagne only
Print out the price of Fries only
'''
# write and test your code here 
# print(food["Lasagna"])
# print(food["Fries"])

'''
########### Change the value of a dictionary key ###############
Change the price of hamburger to 20
Change the price of Fries to 3
'''
# write and test your code here 
food["Hamburger"] = 20
food["Fries"] = 3
'''
############ Increase the value of a dictionary key ############
Increase the price of Lasagne by 5
Decrease the price of Pizza by 3
'''
# write and test your code here 
food["Lasagna"]+=5
food["Pizza"]-=3
'''
############### Add a new key/ Value to the dictionary #####################
Add a new menu item => Pasta which cost 15
Add a new menu item => Sandwich which cost 6
'''
# write and test your code here 
food["Pasta"] = 15
food["Sandwich"] = 6
'''
############### Add a new key/ Value to the dictionary #####################
Delete menu item Pasta
'''
# write and test your code here 
del(food["Pasta"])

'''
########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of food item that you sell
# only display the keys
'''
# write and test your code here 
for i in food:
    print(i)

'''
########### Loop through to Retrieve Values ##################
Write a for loop, and only print out the price
'''
# write and test your code here 
for i in food:
    print(food[i])

'''
########### Loop through to Retrieve Key and Values ##################
Write a for loop, and print out the menu key and values
e.g.
Hamburger costs $10.00
Pizza costs $18.50
'''
# write and test your code here 
for i in food:
    type = i
    cost = food[i]
    print(f"{type} costs ${cost}")
# print(food)
'''
#################### Challenge 1 ######################################
Write a program to calculate how much money you need to buy all the items in the menu.
'''
# write and test your code here 
total = 0
for i in food:
    total+=food[i]
print(total)
'''
############### Challenge 2 ##########################################
Write a program to determine the most expensive item in the menu
'''
# write and test your code here 
highest = 0
name = ""
for i in food:
    if food[i] > highest:
        highest = food[i]
        name = i
print(name)
'''
################ Challenge 3 ########################################
#### Due to inflation, prices have increased. Update all the prices by 10%
'''
# write and test your code here 
for i in food:
    food[i] += food[i]*(1/10)
print(food)
'''
################ Challenge 4 ########################################
Upgrade this system where you ask customers what they want, and display the price 
# you can check if a key exists in a dicionaty, by using the 'in' keyword
# for example: if 'hamburger' in menu: will return true if hamburger exists 

Example:

Hello, What is your name? John
>>> Hi John, what would you like to eat? Laksa
>>> I'm sorry John, we don't sell Laksa. 

Hi John, what would you like to eat? Hamburger
>>> Great choice! Please pay $10.00. Your order will be delivered soon!
Hi John, what would you like to eat? Exit

Ok, bye!
'''
# write and test your code here 
name = input("Hello, What is your name? ")
while True:
    food_name = input(f"Hi {name}, what would you like to eat? ")
    if food_name == "Exit":
        print("Ok, bye!")
        break
    elif food_name not in food:
        print(f"I'm sorry {name}, we don't sell {food_name}")
        break
    else:
        print(f"Great choice! Please pay ${food[food_name]}. Your order will be delivered soon!")