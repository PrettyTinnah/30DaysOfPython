# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python this one
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# 33. Use the new line escape sequence to separate the following sentences.
#     ```py
#     I am enjoying this challenge.
#     I just wonder what is next.
#     ```
# 34. Use a tab escape sequence to write the following lines.
#     ```py
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
#     ```
# 35. Use the string formatting method to display the following:

# ```sh
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# ```

# 36. Make the following using string formatting methods:

# ```sh
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
listing = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

final = '# '.join(listing)
print(final, end = "\n\n")

print("I am enjoying this challenge.\nI just wonder what is next.\n")

print("Name\t\tAge\t\tCountry\t\tCity\nCi-cada\t\t22\t\tKenya\t\tNairobi")

radius = 10
area = 3.14 * radius ** 2
string_f = 'The area of circle wwith radius %d is %d meters square.' %(radius,area)
print(string_f)

num_1 = 8
num_2 = 6
add = '{} + {} = {}'.format(num_1,num_2, num_1+num_2)
sub = '{} - {} = {}'.format(num_1,num_2, num_1-num_2)
div = '{} / {} = {:.2f}'.format(num_1,num_2, num_1/num_2)
mod = '{} % {} = {}'.format(num_1,num_2, num_1%num_2)
flr = '{} // {} = {}'.format(num_1,num_2, num_1//num_2)
exp = '{} ** {} = {}'.format(num_1,num_2, num_1**num_2)


print(add)
print(sub)
print(div)
print(mod)
print(flr)
print(exp)