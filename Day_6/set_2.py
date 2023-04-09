# ### Exercises: Level 2
# 1. Unpack siblings and parents from family_members
# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# 1. Slice out the first three items and the last three items from food_staff_lt list
# 1. Delete the food_staff_tp tuple completely
# 1. Check if an item exists in  tuple:

# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country

#   ```py
#   nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#   ```

fruits = ('mango', 'banana')
vegetables = ('kales', 'cabbage')
animal_prod = ('Milk','Pork')

food_stuff_tp = fruits + vegetables + animal_prod


food_stuff_lt  = food_stuff_tp[:]

print(food_stuff_lt)
mid_food = food_stuff_tp[2:4]

print("The middle is", mid_food)

first_three = food_stuff_lt[0:3]

del food_stuff_tp

if 'Milk' in food_stuff_lt:
    print(True)
else:
    print(False)
    
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries, end="\n\n\n")
print("Checking for Estonia")
if 'Estonia' in nordic_countries:
    print(True,"It is in")
else:
    print(False,"It is not")

print("Checking for Iceland")
if 'Iceland' in nordic_countries:
    print(True,"It is in")
else:
    print(False,"It is not")
    