# 1. Create  an empty dictionary called dog
# 2. Add name, color, breed, legs, age to the dog dictionary
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# 4. Get the length of the student dictionary
# 5. Get the value of skills and check the data type, it should be a list
# 6. Modify the skills values by adding one or two skills
# 7. Get the dictionary keys as a list
# 8. Get the dictionary values as a list
# 9. Change the dictionary to a list of tuples using _items()_ method
# 10. Delete one of the items in the dictionary
# 11. Delete one of the dictionaries

dog = {}
dog['Name'] = 'Patch'
dog['color'] = 'Brown'
dog['breed'] = 'Japannese'
dog['legs'] = 'hairy'
dog['age'] = 3
print(dog)
student = {
    'F_name':'Juma',
    'S_name':'Kandie',
    'Gender':'Male',
    'Age':23,
    'Is Married':False,
    'Skills':['Python','Java','C','C++'],
    'Country':'Kenya',
    'City':'Nairobi',
    'Address':{'Street':'Busara','P-Code':'1028-01001'}
}

print("The legth of student dictionary is: ", len(student))

print("The value of skills is:", student['Skills'], "The datatype", type(student['Skills']))

student['Skills'].insert(-1,'SQL')
print(student['Skills'])

print("The Key's are", student.keys())
print("The vales are", student.values())

list_students = student.items()
print(list_students)

del dog
del student['Is Married']
print(student)