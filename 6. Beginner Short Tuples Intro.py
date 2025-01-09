#Talking about Tuples
#This is a very short into to tuples.
#Tuples are immutable. Once thery are created, they cannot be changed or modified. 

#The code below should show an error because tuples cannot be changed.
tup = ('Oranges','Apples','Bananas')
tup[1] = 'Cherries' 
print(tup)

#using tuples protects data 
#you can also concatenate tuples
tup2 = (12, 14)
tup3 = tup + tup2
print(tup3)
#tuples are immutable data structures