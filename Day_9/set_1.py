# 1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#     ```sh
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
#     ```
# 2.  Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#     ```sh
#     Enter your age: 30
#     You are 5 years older than me.
#     ```
# 3.  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# ```sh
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ```


age = int(input("Enter your age: "))
print("You are old enough to learn to drive") if age > 18 else print("You need", 18-age, "more years to learn to drive")

my_age = int(input("Enter your age: "))

if my_age > 25:
    print("You are", my_age - 25,"years older than me")
else:
    print("I am", 25 - my_age," years older than you")
    
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))

if num_1 > num_2:
    print(num_1,"Is greater than", num_2)
else:
    print(num_2,"Is greater than", num_1)
    