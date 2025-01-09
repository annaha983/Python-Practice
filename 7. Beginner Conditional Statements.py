#Conditional Statements
#This is a very basic intro to Conditional Statements
#If else principle: If a condition is met the initial action is performed, else an alternative is performed. 
#i.e. if it is raining, then take an umbrella: otherwise leave it at home. 

if 3 < 2: 
    print("hello")
else: 
    print("condition is not true")

#conditions are made using relational operators
#relational operators: < > <= >= == !=
if 5==3: 
    print("hello?")
else: 
    print("condition is not true")

#Can use with assigned variables
age = 16
if age <= 15: 
    print("You are younger than 16.")
elif age == 16: 
    print("You are 16.")
elif age == 17:
    print("You are 17.")
else: 
    print("You are older than 16")

#can also use if, elif, else with ranges
if age < 13: 
    print("You are a child.")
elif age >= 13 and age <= 18: 
    print("You are a teenager.")
else: 
    print("You are an adult.")
    
#can also use if, elif, else with or
if 5 > 3 or 2 > 1: 
    print("See Ya later!")
else: 
    print("Goodbye Now.")