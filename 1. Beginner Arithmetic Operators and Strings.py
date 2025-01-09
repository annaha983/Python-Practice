#arithmetic operators and strings
#This is extremely basic practice of utilizing operators, strings, and slicing. 
#It also utilizes numerically defined functions to perform arithmetic. 

age1 = 12
age2 = 18

print(age1 + age2)
print(age1 - age2)

print(age1 * age2)
print(age1 / age2)

#modulus is a function that provides the remainder of a division operation
print(age1 % age2)
print(age2 % age1)

#strings
sent1 = "Today is a beautiful day."

first_name = "Anna"
last_name = "Renee"
print(first_name + " " + last_name)

print("hi" * 10)

sent = "Anna was playing basketball"
print(sent[0:4])
#this is called a slice and only performs the action on the designated number of characters in the string
print(sent1[0:5])