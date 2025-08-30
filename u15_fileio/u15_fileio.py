# import random
# ello = open("Filename.txt","w")
# ello.write("This is the best day of my life after tomorrow")
# ello.close()    
# count =1
# newfile = open("Filename.txt","r")
# content = newfile.read()
# for i in content:
#     if i == "a":
#         count+=1
# print("There were", count,"letter a in the sentence")


# with open("filename.txt","w") as newfile:
#     daylist = newfile.readlines()
#     for day in daylist:
#         print(day)
# randay = random.choice(daylist)
# print("radom day:", randay)
# planetslist = ["murcury", "Venus", "earth", " mars", "jupiter"]

# with open("Planet.txt", "w") as fobj:
#     fobj.writelines(planetslist)



lst = []
while True:
    task = input('What do you want to do today?')
    lst.append(task+ "\n")
    proceed = input('Enter "N" to cancel')
    if proceed.upper() == "N":      
        with open("Tasks.txt","w" ) as Dailytasks:
            Dailytasks.writelines(task)
    else:
        break


# A text file shapes.txt stores a list of shapes with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. 
# The first value in each file will be joined, for example, star and red. 

# The data is stored in a global dictionary with the identifier data_stored. 