# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
import math
def add(num_1, num_2):
    sum = num_1 + num_2
    print("The sum is", sum)

add(1,2)

def area(r):
    
    c_area = r**2 * math.pi
    print("The area is",c_area)
area(4)

def add_all_nums(num):
    dig = 0
    for i in range(num+1):
        dig += i
        #print(i)
    
    print(dig)
add_all_nums(5)

#°F = (°C x 9/5) + 32
def temp_conv(temp):
    f = (temp*(9/5)) + 32
    final = "%d to fahnreheit is %.3f" %(temp,f)
    print(final)
    
temp_conv(67)
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer
def season(month):
    autum = ['September','October','November']
    winter = ['December','January','February']
    spring= ['March','April','May']
    summer= ['June','July','August']
    if month in autum:
        print("Autum is the season")
    if month in spring:
        print("Spring is the season")
    if month in winter:
        print("Winter is the season")
    if month in summer:
        print("Summer is the season")
        
check = input("Enter the month: ")

season(check)