# 1.  Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

# ```py
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# ```

# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# 1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
# 1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics
def evens_and_odds(num):
    count_ev = 0
    count_od = 0
    i = 0
    j = 0
    while i <= num:
        if i % 3 == 0:
            count_od += 1
        i += 1
        
    while j <= num:
        if j % 2 == 0:
            count_ev += 1
        j += 1
    
    print("The number of odds are", count_od,"\nThe number of evens are", count_ev)

evens_and_odds(100)

def factorial(num):
     i = num
     start = 1
     while i  > 0:
         start *= i
         i -= 1
         
     print("Factorial of", num,"is", start)
    
factorial(5)
def is_empty(dig):
    if dig == None:
        print("empty")
    else:
        print(dig)

is_empty(7)
#They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lis):
    tot = len(lis)
    all, i = 0, 0
    while i <= tot - 1:
        all += lis[i]
        i+= 1
    print(all/tot)
    
def calculate_median(lis):
    print(statistics.median(lis))
    
def calculate_range():
    print()
    
def calculate_variance(lis):
    
    tot = len(lis)
    mean = sum(lis) / tot
    dev = [(x - mean)**2 for x in  lis]
    
    var = sum(dev) / tot
    
    print(var)
    
def calculate_std(lis):
    
    print(statistics.pstdev(lis))
    
calculate_mean([1,2,3,4,5,6,7])
calculate_median([1,2,3,4,5,6,7])
# calculate_range([1,2,3,4,5,6,7])
calculate_std([1,2,3,4,5,6,7])
calculate_variance([1,2,3,4,5,6,7])