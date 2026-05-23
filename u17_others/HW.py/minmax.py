###############################################################
# Scenario: Employee Performance Review

# Finding Maximum, Minimum, and Average Performance Scores 
# Without Built-in Functions
# YOU CANNOT USE ANY PYTHON INBUILT FUNCTIONS TO DO THIS.

# A company conducts annual performance reviews for employees. 
# Each employee is given a performance score out of 100. 
# The HR department wants to:

# - Identify the top-performing employee (highest score).
# - Identify the lowest-performing employee (lowest score).
# - Calculate the average performance score, rounded to 2 decimal places.
# - Identify underperforming employees (those with scores below 50) 
#    -> save them into another dictionary called non_performers.
#   and print a performance warning message to all of these employees.

performance_scores = {
    'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
    'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
    'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
    'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# write your code here
max_score = 0
highest_name = ''
low_score = 100
lowest_name = ''
count = 0
total_scores = 0
non_performing_dict = {}
for i in performance_scores:
    score = performance_scores[i]
    if score>max_score:
        max_score = score
        highest_name = i
print(highest_name)
for e in performance_scores:
    score = performance_scores[e]
    if score<low_score:
        low_score = score
        lowest_name = e
print(lowest_name)
for a in performance_scores:
    total_scores+=performance_scores[a]
    count+=1
print(round(total_scores/count,2))
for r in performance_scores:
    if performance_scores[r]<50:
        non_performing_dict[r] = performance_scores[r]
        print(f"Work harder or you will be fired, {r}")
print(non_performing_dict)