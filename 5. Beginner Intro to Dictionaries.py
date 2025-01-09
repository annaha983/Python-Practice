#Introduction to Dictionaries
#Dictionaries are different than lists. 
#Dictionaries associate values to keys. Keys should be unique to properly recall the correct value. 
#This is a very basic practice sheet. 

#Below is a list
students_list = ['Chandler', 24,'Rachel', 23,'Ross', 25,'Monica', 24]
print(students_list)

#Below is a dictionary
students_dict = {'Chandler': 24,'Rachel': 23,'Ross': 25,'Monica': 24}
print(students_dict)
print(students_dict['Chandler'])

#this recalls the value associated with chandler in the dictionary
print("Chandler is", students_dict['Chandler'], "years old.")

#update 
students_dict['Rachel'] = 24

#delete
del students_dict['Ross']

#make sure each key in the dictionary is unique for correct accessing.
#use len again to find the number of entries/keys in the dictionary.
print(students_dict)
print("There are", len(students_dict), "in the student dicitonary.")
