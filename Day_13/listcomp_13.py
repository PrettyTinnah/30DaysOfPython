# list comprehension and all
name = 'Jussie'

namel = list(name)

hmm = [i for i in namel]
if 'e' in hmm:
    print(True)
else:
    print(False)
    
    
odd_numbers = [i for i in range(21) if i % 3 == 0] #list of odd numbers

odd_numbers_squares = [(i,i**2) for i in range(21) if i % 3 == 0] #list of tuples of odd square numbers


print(odd_numbers)
print(odd_numbers_squares)


odd = lambda a, b : a * b

print(odd(1, 2))

checkers = [(i, 1, i**2, i**3, i**3,i**4,i**5,i**6) for i in range(11)]

print(checkers)

listing = [[[1,2,3]], [[4,5,6]],[[7,8,9]]]
sorteds = [sub for sublist in listing for subsublist in sublist for sub in subsublist]

print(sorteds)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_dicts = [{'country': t[0].upper(), 'city': t[1]} for sublist in countries for t in sublist]

print(country_dicts)

# Here, the list comprehension first iterates over each sublist in countries,
# and then over each tuple in each sublist. For each tuple, 
# it creates a new dictionary with the keys "country" and "city", 
# where the value of "country" is the uppercased first element of the tuple (i.e., the country name), 
# and the value of "city" is the second element of the tuple (i.e., the capital city). 
# The resulting list of dictionaries is collected into the variable country_dicts.

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [[country.upper(), country[:3].upper(), capital] for sublist in countries for country, capital in sublist]

print(new_list)
# Here, the list comprehension iterates over each sublist in countries and then over each tuple in each sublist.
# t[0] extracts the first element (i.e., the country name) from each tuple, 
# and the resulting list of country names is collected into the variable names.

name = [(i, 1, i**2, i**3, i**4, i**5, i**6) for i in range(11)]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

name_strings = [' '.join(t) for sublist in names for t in sublist]

print(name_strings)

# Here, the list comprehension first iterates over each sublist in names,
# and then over each tuple in each sublist. For each tuple, 
# it creates a new string by concatenating its two elements with a space between them using the join method.
# The resulting list of strings is collected into the variable name_strings.
