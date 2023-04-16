# 6. Write a function called calculate_slope which return the slope of a linear equation
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# ```py
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# ```
import math
def reverse_list(li):
    i = 4
    while i >= 0:
        print(li[i], end=", ")
        i -= 1

print(reverse_list([1, 2, 3, 4, 5]))

def print_list(lis):
    
    for i in lis:
        print(i, end=", ")

print_list([1, 2, 3, 4, 5])
print()
#solution = (y2-y1)/(x2-x1)
def slope(x,y,x2,y2):
    solution = (y2-y)/(x2-x)
    print("The gradient is: ", solution)
    
slope(4,3,2,4)

def quad(a,b,c):
    #form = (-b - sqrt(b**2 - 4ac))/2a
    #form = (-b + sqrt(b**2 - 4ac))/2a
    
    sol = b**2
    sol2 = 4*a*c
    total = sol - sol2
    total *= -1
    print(total)
    d = math.sqrt(total)
    
    x_1 = (-b - d) / 2*a
    
    x_2 = (-b + d) / 2*a
    
    print("X = ", x_1,"or X = ", x_2)

quad(2,1,4)
    
    