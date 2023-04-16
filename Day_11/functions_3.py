# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# ```py
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# ```

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# ```py
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
# ```

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# ```py
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
# ```

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def cap(lis):
    capit = []
    for name in lis:
        capit.append(name.upper())
    print(capit)

cap(['Congo','Jumia','Sychelles'])

def check(lis, item):
    print(lis)
    lis.append(item)
    print(lis)

check(['Banana','Mango','Apple'],'Pear')

def remove_item(list,deleted):
    
    print(list)
    list.remove(deleted)
    print(list)
remove_item(['Banana','Mango','Apple'], 'Apple')

def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    
    print("The sum is", sum)
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(num):
    sum = 0
    for i in range(num+1):
        if i % 3 == 0:
            sum += i
    print("The sum of odd numbers betweeen",num,"is",sum)
            
def sum_of_even(num):
    sum = 0
    for i in range(num+1):
        if i % 2 == 0:
            sum += i
    print("The sum of even numbers betweeen",num,"is",sum)

sum_of_even(90)
sum_of_odds(90)
        