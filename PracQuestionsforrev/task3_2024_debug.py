#3:57 started   7min  ended 4:04
# 2024 – Task 3 [10]
# A program is needed to find out whether the size of a parcel for posting is small medium or large.
# The program:
# •	takes as the length (longest side), width (second longest side) and depth (shortest side) of the parcel
# •	calculates whether the parcel is large, medium, or small
# •	outputs the size of the parcel.

# The parcel is:
# •	large – if the length, width and depth are all greater than 50.
# •	medium – if the length and width are greater than 50, but the depth is 50 or less.
# •	small – if either the length or the width is 50 or less.
# The program loops until the user does not want to check the size of any more parcels.
# You do not need to consider any validation for the inputs.

# The following program was written to meet the criteria.

flag = True  #True not false because if not it will ont run
while flag:
	length = float(input("What is the length of the parcel?"))
	width = float(input("What is the width of the parcel?"))
	depth = float(input("What is the depth of the parcel?"))
	if length > 50 and length > 50 and depth > 50:
		parcel_size = "large"  #parcel not parecel
	elif length > 50 and width > 50 and depth <= 50:     #<= not > and and not or
		parcel_size = "medium"    #parcel_size not parcel-size
	else:           #else not elif as there is no confition set
		parcel_size = "small"
	print(parcel_size)     #didnt output parcel size
	more_parcel = input("Do you want to enter another parcel? Y or N") 
	if more_parcel == "N":   #== not = and "N" not N
		flag = False #false not true
		
# Open the file PARCELS.py
# Save the file as MY_PARCELS_2024___ .py
# Identify and correct the errors in the program so that it works according to the requirements given.
# Save your program. [10]
