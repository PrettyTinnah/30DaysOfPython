# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

#    ```sh
#    The sum of all numbers is 5050.
#    ```

# 1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#     ```sh
#     The sum of all evens is 2550. And the sum of all odds is 2500.
#     ```
sum = 0
for i in range(100):
    sum = sum + i
    print("The sum of all numbers is", sum)

sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even +=i
    else:
        sum_odd += i
print("Sum of all evens is",  sum_even, "And the sum of all odds is", sum_odd)
    