import math
# # 				     START:2:52PM		        END:3:12
# # A 2-player game is being programmed.
# # The following program allows each player, in turn, to enter the names of 5 animals. 
# # It converts the name of each animal to lower case. 
# # Each animal entered by player 2 is their guess for the animal entered by player1.
	
# # num_of_animals = 5
# # for x in range(num_of_animals):
# # 	p1_animal = input("Player 1, please enter an animal: ")
# # 	p1_animal = p1_animal.lower()
# # 	p2_guess = input("Player 2, please enter your guess: ")
# # 	p2_guess = p2_guess.lower()
	
# # Open the fie ANIMALGAME.py
# # Save the file as ANIMAL_2023_<your name>_<centre number>_<index number>.py

# #============================================================
# # 1.	Edit the program to allow player 1 to keep entering animals until that player does not want to enter any more. 
# # All animals entered by player 1 must be stored in a list. 

# # Once all animals have been entered by player 1, player 2 will enter a single guess. 
# # All inputs and outputs must have suitable messages. 
# # Save your program.  [4 marks]
# # -----------------------------------------------------------

# # List, list append, loops are wrong. 
# # 1.5 / 4

# # p1_animals = []
# # p1_choice = ""
# # while True:
# # 	p1_animal = input("Player 1, please enter an animal: ")
# # 	p1_animals.append(p1_animal)
# # 	p1_choice = input("Enter STOP to end")
# # 	if p1_choice == "STOP":
# # 		break
# # p1_animal = p1_animal.lower()
# # p2_guess = input("Player 2, please enter your guess: ")
# # p2_guess = p2_guess.lower()





# #============================================================
# # 2.	Save your program as ANIMAL2_2023_<your name>_<centre number>_<index number>.py 

# # Edit your program to search the list of animals to find the guess entered by player 2. 
# # Player 2 has a score that starts at 0. If the guess entered by player 2 is found in the list:
# # •	the animal is removed from the list
# # •	the score for player 2 is incremented by 1
# # Save your program. [3 marks]
# # -----------------------------------------------------------

# # code is correct for second part, but first part is all wrong...
# # 1.5 - 2 / 3

# # score = 0
# # p1_animals = []
# # p1_choice = ""
# # while True:
# # 	p1_animal = input("Player 1, please enter an animal: ")
# # 	p1_animals.append(p1_animal)
# # 	p1_choice = input("Enter STOP to end")
# # 	if p1_choice == "STOP":
# # 		break
# # p1_animal = p1_animal.lower()
# # p2_guess = input("Player 2, please enter your guess: ")
# # p2_guess = p2_guess.lower()
# # if p2_guess in p1_animals:
# # 	score+=1



# #============================================================
# # 3.	Save your program as ANIMAL3_2023_<your name>_<centre number>_<index number>.py

# # Edit your program to allow player 2 to keep entering guesses until they enter 
# # an animal that is not found in the list, or until the list is empty. 
# # When player 2 enters an animal that is not found in the list:
# # •	the game ends and informs player 2 the game is over 
# # •	a message is displayed showing: 
# # o	player 2 their score “
# # o	the animals that are still in the list.
# # All inputs and outputs must have suitable messages. Save your program. [3 marks]
# # -----------------------------------------------------------

# ### 

# # p2_score = 0
# # p1_animals = []
# # p1_choice = ""
# # num_of_animals = 5
# # while True:
# # 	while p1_choice != "STOP":
# # 		p1_animal = input("Player 1, please enter an animal: ")
# # 		p1_animals.append(p1_animal)
# # 		p1_choice = input("Enter STOP to end")
# # 	print(p1_animals)
# # 	p1_animal = p1_animal.lower()
# # 	p2_guess = input("Player 2, please enter your guess: ")
# # 	p2_guess = p2_guess.lower()
# # 	if p1_animals == []:
# # 		print("You won")
# # 		print(f" you scored{p2_score} points")
# # 		break
# # 	elif p2_guess in p1_animals:
# # 		p1_animals.remove(p2_guess)
# # 		p2_score+=1
# # 	else:
# # 		print("Game over")
# # 		print(f" you scored{p2_score} points")
# # 		print(p1_animals)
# # 		break



# score = 0
# p1_animals = []
# p1_choice = ""
# while p1_choice != "STOP":
# 	p1_animal = input("Player 1, please enter an animal: ")
# 	p1_animal = p1_animal.lower()
# 	p1_animals.append(p1_animal)
# 	p1_choice = input("Enter STOP to end")
# 	if p1_choice == "STOP":
# 		break
# while True: 

#     p2_guess = input("Player 2, please enter your guess: ")
#     p2_guess = p2_guess.lower()
#     if not(p2_guess in p1_animals):
#         print("You lost")
#         print(f'remaining animals are {p1_animals}')
#         print(f"you scored {score} points")
#         break
#     else:
#         score+=1
#         p1_animals.remove(p2_guess)
#     if len(p1_animals) == 0:
#         print("You won!!!!")
#         print(f"you scored {score} points")
#         break









# START 3:58   END: 4:18
# list_username = ["StudentNo1", "JaneJones", "ABC123"] 
# username = input("Please enter a username: ")
# while True:
#     if not(username in list_username):
#         list_username.append(username)
#         break
#     else:
#         username = input("Please enter a username that doesnt already exist: ")
# password = input("Please enter a password: ") 


#2:
# special_chars = ["@","!","/","?"]

# list_username = ["StudentNo1", "JaneJones", "ABC123"] 
# username = input("Please enter a username: ")
# while True:
# 	if not(username in list_username):
# 		list_username.append(username)
# 		break
# 	else:
# 		username = input("Please enter a username that doesnt already exist: ")

# while True:
#     password = input("Enter a password")
# 	gotdigit = False
# 	gotspecial = False
# 	longenough = False
    
# 	for i in password:
# 		if i.isdigit():
# 			gotdigit = True
# 		if i in special_chars:
# 			gotspecial = True
# 		if len(password) >=8:

# 			longenough = True
# 	if gotdigit and gotspecial and longenough:
# 		break
# 	else:
# 		comment = ''
# 		if gotdigit == False:
# 			comment+="with digits "
# 		if gotspecial == False:
# 			comment+="with special chars "
# 		if longenough == False:
# 			comment+"longer"
# 		password = input(f"Please enter another password {comment}: ")











#				Start: 4:35                    End: 4:55     ended at :4:47

# capital_cities = { 
# 'singapore':'Singapore', 
# 'japan':'Tokyo', 
# 'australia':'Canberra', 
# 'england':'London', 
# 'france':'Paris', 
# 'germany':'Berlin' 
# } 
# country = input("Please enter the name of a country: ") 
# country = country.lower()
# print(capital_cities[country])
# remove = input("Would you like to remove any of the entries? (Y or N): ") 
# add = input("Would you like to add a new entry? (Y or N): ")

#2

# capital_cities = { 
# 'singapore':'Singapore', 
# 'japan':'Tokyo', 
# 'australia':'Canberra', 
# 'england':'London', 
# 'france':'Paris', 
# 'germany':'Berlin' 
# } 
# country = input("Please enter the name of a country: ") 
# country = country.lower()
# print(capital_cities[country])
# remove = input("Would you like to remove any of the entries? (Y or N): ") 
# if remove == "Y":
# 	remove_country = input("Which country do you want to remove? ")
# 	remove_country = remove_country.lower()
# 	del(capital_cities[remove_country])
# add = input("Would you like to add a new entry? (Y or N): ")


#3
# capital_cities = { 
# 'singapore':'Singapore', 
# 'japan':'Tokyo', 
# 'australia':'Canberra', 
# 'england':'London', 
# 'france':'Paris', 
# 'germany':'Berlin' 
# } 
# country = input("Please enter the name of a country: ") 
# country = country.lower()
# print(capital_cities[country])
# remove = input("Would you like to remove any of the entries? (Y or N): ") 
# if remove == "Y":
# 	remove_country = input("Which country do you want to remove? ")
# 	remove_country = remove_country.lower()
# 	del(capital_cities[remove_country])
    
# add = input("Would you like to add a new entry? (Y or N): ")
# if add == "Y":
# 	add_country = input("Which country would you like to add?")
# 	add_capital = input("Which capital would you like to add?")
# 	capital_cities[add_country] = add_capital
# 	print(capital_cities)

sentence = "computing is fun"
print("int".find("it"))

import random
try:
    math.sqrt(-1)
except ValueError:
    print("Cannot calculate")

users = {"leonard": 1001, "Jacob": 1234}
def finduser():
    user = input("Enter your user ")
    if users.find(user) == -1:
        print("You are currently searching for a person that doesnt exist.")
    else:
        passwordcheck = users[user]
        password = input(f"Enter your password, {user} ")
        if password == passwordcheck:
            print(f"Welcome back, {user}!")
        else:
            for i in range(3):
                password = input(f"Enter your password, {user} ")
                if password == passwordcheck:
                    print(f"Welcome back, {user}!")
                    exit()
            print("Try again later.")

