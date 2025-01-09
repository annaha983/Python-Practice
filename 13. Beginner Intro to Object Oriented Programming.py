#Introduction to Object Oriented Programming - OOP
#Most projects have an object oriented design that utilizes classes, and objects. 
#Class: defines object
#Properties: describes the object
#Methods: what the object does

class Person:                           #This is Class
    def __init__(self, name, age):      #This denotes the properties
        self.name = name
        self.age = age

    def getName(self):                  #This is the method
        return self.name
    
    def getAge(self):                   #This is the method
        return self.age
    
p1 = Person("Bob", 22)                  #p1 is the object
print(p1.getName()," is ", p1.getAge(), ".")
#now p1 is bob and the attributes can be recalled from the properties of bob using p1.getName or p1.getAge. 


#Object Oriented Programming using class inheritance 
#OOP - Class inheritance: Creates a parent class to make more sub classes off of. 

class Car:                  #This is the parent class. 
    def __init__(self):     #These are the properties.
        self.wheels = 4
        self.seats = 5


    def drive(self):        #This is the method
        print("Driving a car . . . ")

myCar = Car()           #This links the object with the class
myCar.drive()           #This calls the function drive that is associated with the class.


class SportsCar(Car):           #This class inherits properties from the parent class Car. 
    def __init__(self): 
        super().__init__()              #Super.__init__ executes the innit of the parent car class
        self.engine_power = '400 HP'      #it keeps the attributes of the parent, and can modify such as seats. 
        self.seats = 2

    def drive(self):
        print("Driving a sports car . . .")

#making an object below
mySportsCar = SportsCar()        #This defines the object with the class
mySportsCar.drive()             #This calls the function drive associated with the class that prints what is listed. 

#object and class oriented programming makes things easier by allowing common properties or reoccuring, functions, properties or data to be changed or altered all at once. 
#The sub classes will inherit different changes.
 
