# 1. Create an empty tuple
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# 3. Join brothers and sisters tuples and assign it to siblings
# 4. How many siblings do you have?
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

name = tuple()

brother = ('Hezzy', 'Jermain')
sister = ('Migalle', 'Hope')

siblings = brother + sister

many = len(siblings)
print("I have", many, "siblings")

parents = ('Ruth', 'Tobias')
family_members = siblings + parents
print(family_members)

young = family_members[0:3]

print("Siblings are", young)
old = family_members[-2:]

print("The parents are", old)