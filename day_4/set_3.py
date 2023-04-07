# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
# 11. Replace the word coding in the string 'Coding For All' to Python.
# 12. Change Python for Everyone to Python for All using the replace method or other methods.
# 13. Split the string 'Coding For All' using space as the separator (split()) .
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.


# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.

word = "Coding For All"
print("\nFinding the word coding position", end = ":")
pos = word.find("Coding")
print(pos)

print("\nReplacing Coding with Python", end = ": ")
rep = word.replace("Coding","Python")
print(rep)

print("\nSplitting the word", end = ": ")
new = word.split(' ')
print(new)

socials = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("\nPrinting my socials split", end = ": ")
print(socials.split(','))

















