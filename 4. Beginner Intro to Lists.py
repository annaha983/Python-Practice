#Introduction to lists
#Lists are able to be changed, appended, splicing, and have values deleted. 

shopping_list = ['Apples', 'Oranges', 'Bananas', 'Cheese']
#index 0 is the first item
print(shopping_list[0])
print(shopping_list[1])

#can also use spicing to display a certain range of the list
print(shopping_list[0:2])

#use .append to add to list
shopping_list.append('Blueberries')
print(shopping_list)

#to replace 
shopping_list[0] = 'Cherries'
print(shopping_list)

#to delete
del shopping_list[1]
print(shopping_list)

#to show length of list
print("The number of items on the shopping list are", len(shopping_list),".")

shopping_list2 = ['Butter','Bread','Jam','Penut Butter']
print(shopping_list + shopping_list2)
total_list = (shopping_list2 + shopping_list)
print(total_list)

#you can also show the max and min of number lists
number_list = [1,2,3,4,5,100]
print("The largest number in the list is", max(number_list),".")
print("The smallest number in the list is", min(number_list),".")