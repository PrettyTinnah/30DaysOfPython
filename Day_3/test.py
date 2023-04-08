#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#Day 3 
print("The Divisbility of 2 check")
num = int(input("Enter the number: "))

if num % 2 != 0:
    print("Not diviscible")
else:
    print("Diviscible")
    
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Check if floor division is equal to int value")
div = 7 // 3

check = 2.7
check = int(check)

if div != check:
    print("Not Equal")
else:
    print("Equal")

#Check if type of '10' is equal to type of 10

print("Checking type equality")
dig_1 = '10'
dig_2 = 10

if type(dig_1)  == type(dig_2):
    print("They are equal")
else:
    print("They are not")
print("Checking type int equality")
num_1 = '9.8'
num_1 = float(num_1)
num_1 = int(num_1)
num_2 = 10

if num_1 == num_2:
    print("Equal")
else:
    print("Not eual")
