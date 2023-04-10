# ## Exercises: Level 1

# 1. Find the length of the set it_companies
# 2. Add 'Twitter' to it_companies
# 3. Insert multiple IT companies at once to the set it_companies
# 4. Remove one of the companies from the set it_companies
# 5. What is the difference between remove and discard


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print("The length of the it_companies is", len(it_companies))

it_companies.add('Twitter')
print("After addition", it_companies)

multiple = ('Tesla','Mitsubishi','Mercedes')
it_companies.update(multiple)
print("After adding multiple companies", it_companies)

it_companies.pop()
#or 
it_companies.remove('Mercedes')

print("After removing one of the companies", it_companies)
#discarding is deleting 