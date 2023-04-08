#Day 3 working with circle 
import math 
radius = int(input("Enter the radius: "))

#calculating area 
#formula pi.r^2

area = math.pi * radius * radius

#calculating the circumference 
#dormula pi * radius * 2

circumference = radius * 2 * math.pi

#showing results

print("The area is: ", area)
print("The circumference is: ", circumference)