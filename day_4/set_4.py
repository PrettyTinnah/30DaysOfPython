# 15. What is the character at index 0 in the string _Coding For All_.
# 16. What is the last index of the string _Coding For All_.
# 17. What character is at index 10 in "Coding For All" string.
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.

word = "Coding For All"

print("Printing character at index 0", end = ": ")
c = word[0]
print(c)
print("/Printing the last index", end = ": ")
last = word[13]
print(last)
print("Printing the last 10'th character", end = ": ")
tenth = word[10]
print(tenth)

new = "Python For Everyone"
first = new[0]
second = new[7]
last = new[11]

acrym = first + second + last

print("\nPrinting the acronym of 'Python For Everyone'", end = ": ")
print(acrym)

another = "Coding For All"

first = another[0]
second = another[7]
third = another[11]

print("\nPrinting acronym of 'Coding For All", end = ": ")

acrym = first + second + third
print(acrym)
