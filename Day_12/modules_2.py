import random, string
from random import randint
def random_user_id():
    id = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
    
    return id
def user_id_gen_by_user(a, b):
    
    for i in range(b):
        id = ''.join(random.choices(string.ascii_lowercase + string.digits, k = a))
        print(id)
        
def rgp_color_gen():
    #this will generate random numbers from zero to 255 for each set inclusive of them
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    
    return f"rgb({a},{b},{c})" #this is using the placeholder with a string to print out a specific format

import random

def hexa_colors(n):
    colors = []
    for i in range(n):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors

def rgb_colors(n):
    colors = []
    for i in range(n):
        color = "rgb({},{},{})".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colors.append(color)
    return colors

def generate_colors(select, num):
    if select == 'hexa':
        return hexa_colors(num)
    elif num == 'rgb':
        return rgb_colors(num)
    else:
        exit()


def unique_numbers():
    numbers = random.sample(range(10), 7)
    return numbers

print(unique_numbers())

def shuffle_list(lst):

    shuffled_lst = lst.copy()
    
    random.shuffle(shuffled_lst)
    
    return shuffled_lst
