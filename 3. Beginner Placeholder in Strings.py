#Placeholders in strings
#This is basic practice of using placeholders in strings, and f-strings
# The principle can be applied to an Automated email system - personalized emails

name = "Jake"
print(name + " is 15 years old")
#use placeholder to make easier

name = "Anna"
sentence = "%s is 15 years old."
print (sentence % name)

print(sentence % "Jason")

#format strings
name = "Avi"
print(f"Hello, {name}.")

x = 10 
y = 20
print(f"The sum of x and y is {x + y}.")
#f-strings like this are much easier and cleaner