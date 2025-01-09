#Welcome to functions
#This a basic intro to functions.
#A function compiles many steps into one defined sequence of steps. 

def hi_there(): 
    print(hi_there)
#This will not print anything because the function has no actions or steps in it. 

def greeting(name): 
    print("Hi " + name + "!")

greeting("Avi")
# This will print Hi Avi ! 

#A function be applied as a calculator
def add(numb1, numb2):
    print("The sum is ", numb1 + numb2, ".")

add(10, 20)  

#The result can be saved.
def add(numb3, numb4): 
    return numb3 + numb4

num_sum = add(12,23)
print("The sum is ",num_sum, ".")

#Can further compile: we can return the outputs of a function and use as imputs of another function. 
def mul(numb3, numb4):
    return numb3 * numb4
    print("Hi There")

print("Your product is ", mul(add(1,2), add(3,4)), ".")
#This shows the utilizaiton of a  multiplication function.
# Within the print action, the values to use in the function mul were identified with add(,). 