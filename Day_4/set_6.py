# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28. Does '\'Coding For All' start with a substring _Coding_?
# 29. Does 'Coding For All' end with a substring _coding_?

sent = "You cannot end a sentence with because because because is a conjunction"
sliced = sent[30:54]
print("Slicing out 'because because because' in 'You cannot end a sentence with because because because is a conjunction'", end = ": ")
print(sliced)

sent  = "You cannot end a sentence with because because because is a conjunction"
appear  = sent.index("because")
print("\nPrinting the position of first occurence  of 'Because' in 'You cannot end a sentence with because because because is a conjunction'", end = ": ")
print(appear)

code = '\'Coding For All'
print("\nChecking if Coding For All starts with Coding", end = ": ")
check = code.startswith("Coding")
print(check)

print("\nChecking if Coding For All ends with Coding", end = ": ")
check = code.endswith("Coding")
print(check)