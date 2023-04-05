#Day 2: 30 Days of python programming
import math
#EXERCISE LEVEL 1
#declaration
first_name = "Cipher"
Last_name = "Cicada"
full_name = Last_name + " " + first_name
country = "Kenya"
city = "Nairobi"
age = 22
year = 2023
is_married = False
is_true = True
is_light_on = False
cash, balance = 2000, 200
#Printing them out 
print(first_name)
print(Last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_light_on)
print(is_true)
print(cash, balance)
#EXERCISE LEVEL 1 DONE
#--------------------------------------------------------------
#EXERCISE LEVEL 2 
print(len(first_name))
if len(first_name) > len(Last_name):
    print(True)
else:
    print(False)

num_one, num_two = 5, 4
total, diff, product, division,remainder, exp  = num_one + num_two, num_one - num_two, num_two * num_one, num_one / num_two, num_two & num_one, num_one**num_two
floor_division = num_one // num_two

print("Total is",total,"Diff is",diff,"Product is",product,"Division is",division,"Remainder is",remainder,"To the power is",exp,"Floor division is",floor_division)

#calculating the area of the circle and circumference of it's value radius assigned radius 30 meters 

radius = 30 
#formula pi.r^2
#pi.d

pi = math.pi

_area_of_circle_, _circum_of_circle_  = pi * (radius**2), pi * (radius * 2)
print("Area is: ",_area_of_circle_,"Circumference is: ", _circum_of_circle_)

#taking the radius as user input

radius = int(input("Enter the radius: ")) 
#formula pi.r^2
#pi.d

pi = math.pi

_area_of_circle_, _circum_of_circle_  = pi * (radius**2), pi * (radius * 2)
print("Area is: ",_area_of_circle_,"Circumference is: ", _circum_of_circle_)

#getting user information

f_name = input("Enter your name: ")
l_name = input("Enter last name: ")
age = int(input("Enter your age: "))
country =  input("Ente the country: ")

#showing the information
print("The user is ", f_name, l_name, "of age ", age, "and from ", country)

#end day_2 of #30 Days of Python