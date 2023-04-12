#    1. Here we have a person dictionary. Feel free to modify it!
   
# ```py
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
# ```

#      * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#      * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#      * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#      * If the person is married and if he lives in Finland, print the information in the following format:

# ```py
#     Asabeneh Yetayeh lives in Finland. He is married.
# ```

person={
     'first_name': 'Ephesianse',
     'last_name': 'Cica',
     'age': 22,
     'country': 'Kenya',
     'is_marred': False,
     'skills': ['C++', 'Java', 'C', 'SQL', 'Python'],
     'address': {
         'street': 'Busara',
         'zipcode': '02231'
     }
}
print("Dict has skills key") if 'skills' in person.keys() else print("It does not exist")

if 'skills' in person.keys():
    sett = person['skills']
    print("yes he has python") if 'python' in sett else print("No there is no python ")
    print("He is a software engineer") if 'C++' or 'C' in sett else print("He is a no software engineer")

if person['is_marred'] == 1 and person['country'] == 'Kenya':
    print(person['first_name'], person['last_name'],"Lives in", person['country']+".","He is married")
else:
    print(person['first_name'], person['last_name'],"He is not married but he lives in",person['country'])