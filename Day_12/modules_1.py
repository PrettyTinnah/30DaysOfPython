#all the imports notes 
#statistics - they provide modules for mathematical statistics of numerical data such as mean(), median(), mode() and stdev()
#math modules - mathemaical operations such as rouding off and squareroots for, floor()**to the lowest, ceil()**to the highest, lognum()**logarithms as num as the base
#import * - this imports all the functions in the module 
#import func as alias = this is used to import a certain function with an alias name from a certain module
#string module - for string sets string.ascii_letters for letters, string.digits for the digits, string.punctuation for punctuation marks
#the string module has only one data set from its definition 
#random - has two random and randint(for random integers)

from modules_2 import *

print(random_user_id())

length , total = map(int, input().split())
user_id_gen_by_user(length, total)

print(rgp_color_gen())


print(generate_colors('hexa', 6))
print(generate_colors('rgb', 3))   
print(generate_colors('rgb', 1))   

unique_numbers()



my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)

print(shuffled_list)


