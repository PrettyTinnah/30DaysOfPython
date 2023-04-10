# ### Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# 1. Explain the difference between the following data types: string, list, tuple and set
# 2. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

age = [22, 19, 24, 25, 26, 24, 25, 24]

ages = set(age)

print("The length of age list is",len(age))
print("The legnth of ages",len(ages))

#string is a data type that is a sequence of characters
#list is an orderd set of items
#tuple is a collection on unorederd set of items cannot be changed
#set is a collection of unordersd items which can be changed

sentence = 'I am a teacher and I love to inspire and teach people'

print(sentence.split(' '))
