
# 1. Write a function called is_prime, which checks if a number is prime.
# 1. Write a functions which checks if all items are unique in the list.
# 1. Write a function which checks if all the items of the list are of the same data type.
# 1. Write a function which check if provided variable is a valid python variable
# 1. Go to the data folder and access the countries-data.py file.

# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
from ast import parse
    

def is_prime(num):
    check = False
    if num == 1:
        print("not prime")
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                check = True
                break
            
        if check:
            print("Not Prime")
        else:
            print("Prime")
def if_unique(li):
    check = True
    for i in li:
        if li.count(i) > 1:
            check = False
            break
    if check:
        print("Unique")
    else:
        print("Not unique")
    
def data_type(li):
    
    if type(li) is not type(int):
        print("They are different")
    else: 
        print("They are the same")
        
def var(num):
    try:
        parse('{} = None'.format(num))
        return True
    except SyntaxError:
        return False
    
is_prime(29)
if_unique([1,2,3,4,5,6,7,3])
data_type([1,2,3,4,5,6,7,3])
