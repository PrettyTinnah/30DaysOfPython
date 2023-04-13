# 5. Print the length of the company string using _len()_ method and _print()_.
# 6. Change all the characters to uppercase letters using _upper()_ method.
# 7. Change all the characters to lowercase letters using _lower()_ method.
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
# 9. Cut(slice) out the first word of _Coding For All_ string.


# 5. Print the length of the company string using _len()_ method and _print()_.

company = "Coding For All"
print("The length")
lenn = len(company)
print(lenn)

# 6. Change all the characters to uppercase letters using _upper()_ method.

big = company.upper()
print("\nEffect on upper")
print(big)

low = company.lower()
print("\nEffect on lower")
print(low)

cap = company.capitalize()
print("Effect on Capitalize")
print(cap)

tite = company.title()
print("\nEffect on title")
print(tite)

cas = company.swapcase()
print("\nEffect on Swapcase")
print(cas)

print(cas[7:15]) #starts from index 6 to 15 which 15 is the '\n' and 14 the last lettr 'l'