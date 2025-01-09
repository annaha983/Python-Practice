#While Loops Introduction
#A While Loop Keeps performing an action or function while a condition is true
#Without the while loop you would need to continuously monitor and update. 
#But a While Loop monitors it itself.
c = 0
while c < 5: 
    c = c + 1
    if c == 3: 
        break
    print(c)
#break, continue, and pass can be used in the if statement of the while loop to stop, skip current iteration or continue an action. 

print("     ")

#With Continue
b = 1 
while b < 6: 
    b = b + 1 
    if b == 5: 
        continue 
    print(b)

print("      ")

#With Pass
a = 2 
while (a < 15): 
    a = a + 1 
    if a == 10: 
        pass
    print(a)