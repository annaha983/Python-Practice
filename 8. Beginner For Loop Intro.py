#For loops Introduction
#This is a basic For Loops practice sheet

list1 = ['Apples','Bananas','Cherries']
tup1 = (2, 6, 10)

for item in list1:
    print(item)
#this prints out each item in the list on it's own line

print(" ")

for item in tup1: 
    print(item)
#They perform the same way on the tuple
#For loops are great for navigating data structures. 

print("   ")

#range structures usage below
for i in range(0,10):
    print(i)

print("    ")

#range can also skip numbers, the last number is the count by number
for i in range(0, 11, 2):
    print(i)

print("   ")

for i in range(0, 50, 5):
    print(i)

#you can also nest for loops 
print(" ")

#i iterates over j
for i in range(0, 5):
    for j in range(0, 3):
        print(i * j)