# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


word = "Coding For All"

appear = word.index('C')
print("\nPrinting the first appearance of 'C' in 'Coding For All'", end = ": ")
print(appear)

appear = word.index('F')
print("\nPrinting the first appearance of 'F' in 'Coding For All'", end = ": ")
print(appear)


appear = word.rindex('l')
print("\nPrinting the last appearance of 'l' in 'Coding For All'", end = ": ")
print(appear)

conj = "You cannot end a sentence with because because because is a conjunction"
appear  = conj.index("because")
ll = len(conj)
print("\nPrinting the position of first occurence  of 'Because' in 'You cannot end a sentence with because because because is a conjunction'", end = ": ")
print(appear,ll)

conj = "You cannot end a sentence with because because because is a conjunction"
appear  = conj.rindex("because")
ll = len(conj)
print("\nPrinting the position of last occurence  of 'Because' in 'You cannot end a sentence with because because because is a conjunction'", end = ": ")
print(appear,ll)

