#   1. Write a code which gives grade to students according to theirs scores:
   
#         ```sh
#         80-100, A
#         70-89, B
#         60-69, C
#         50-59, D
#         0-49, F
#         ```
# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer
# 2.  The following list contains some fruits:
#     ```sh
#     fruits = ['banana', 'orange', 'mango', 'lemon']
#     ```
#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list') 

grade = int(input("Enter the scores: "))
if grade >= 90 and grade <= 100:
    print("Your score is A")
if grade >= 70 and grade <= 89:
    print("Your score is B")
if grade >= 60 and grade <= 69:
    print("Your score is C")
if grade >= 50 and grade <= 59:
    print("Your score is D")
if grade >= 0 and grade <= 49:
    print("Your score is F")
    
season = input("Enter the month: ")
if season == 'September' or season == 'October' or season == 'November':
    print("The season is Autum")
if season == 'December' or season == 'January' or season == 'February':
    print("The season is Winter")
if season == 'March' or season == 'April' or season == 'May':
    print("The season is Spring")
if season == 'June' or season == 'July' or season == 'August':
    print("The season is Summer")
    
fruits  = ['banana','orange','mango','lemon']

ad_it = input("Enter the fruit you want to search: ")

if ad_it in fruits:
    print(ad_it,"exists")
else:
    print(ad_it,"does not exist")
    fruits.append(ad_it)
    print(fruits)