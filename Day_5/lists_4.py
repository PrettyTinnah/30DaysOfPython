# 16. Sort the list using sort() method
# 17. Reverse the list in descending order using reverse() method
# 18. Slice out the first 3 companies from the list
# 19. Slice out the last 3 companies from the list
# 20. Slice out the middle IT company or companies from the list
# 21. Remove the first IT company from the list


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("Sorted list")
it_companies.sort()
print(it_companies)

it_companies.reverse()
print("\nCompanies in reversed order", it_companies)

sliced = it_companies[3:6]
print("\nPrinting the 3 first sliced out items", sliced)

next_slice = it_companies[:-3]
print("\nPrinting 3 sliced out last items list",next_slice)

#del it_companies[0]
#it_companies.pop(0)
