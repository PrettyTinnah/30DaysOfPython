# 10. Print the list after modifying one of the companies
# 11. Add an IT company to it_companies
# 12. Insert an IT company in the middle of the companies list
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
# 14. Join the it_companies with a string '#;&nbsp; '
# 15. Check if a certain company exists in the it_companies list.


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('Jumia')

print(it_companies)
it_companies.append('Tesla')
print(it_companies)

it_companies.insert(4,'Neuralink')
print(it_companies)

alpha = it_companies[1]
alpha.upper()
print(alpha.upper())


joined = '# '.join(it_companies)
print(joined)
#else 
print("Alternative", end = ': ')
better = ['Tecno', 'Apple', 'Samsung']

merge = it_companies + better
print(merge)


if 'Facebook' in it_companies:
    print(True)
else:
    print(False)