#using while loop here
#Day 3 tasks

#finding the value of y in an equation y = x^2 + 6x + 9 
#the program only terminates when the value of y is 0 
while True:
    x = int(input("Enter the value of x: "))
    y = (x**2) + (6*x) + 9
    print("Y is : ", y)
    if y == 0:
        print("y is ",y ,"at",x)
        break
    