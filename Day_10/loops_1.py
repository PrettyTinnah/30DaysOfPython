# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#    ```py
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
#    ```

# 4. Use nested loops to create the following:

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```

# 5. Print the following pattern:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(11):
    print(i, end=", ")

a = 11

while a >= 0:
    print(a, end = ", ")
    a -= 1

for i in range(8):
        print("#"*i)

print("\n\n")
for i in range(9):
    for c in range(9):
        print("#", end=(''))
    
    print()

print()
for i in range(11):
        print(i,"x",i,"=",i*i)
        
languages =  ['Python', 'Numpy','Pandas','Django', 'Flask']

for name in languages:
    print(name)
    
print()
print("Even Numbers")
for i in range(101):
    if i % 2 == 0:
        print(i, end=", ")
print()
print("Odd Numbers")
for i in range(100):
    if i % 3 == 0:
        print(i)