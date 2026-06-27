first_name = 'Aryan'
last_name = 'Ahmad'
country = 'Pakistan'
city = 'Multan'
age = 22
is_married = False
skills = ['Python', 'JavaScript', 'HTML', 'CSS', 'Django', 'React']
person_info = {
    'firstname' : 'Aryan' ,
    'lastname' : 'Ahmad',
    'country' : 'Pakistan',
    'city' : 'Multan'
}

# Printing the variables

print('First Name:', first_name)
print('First name length:', len(first_name))
print('Last Name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Is Married:', is_married)
print('Skills:', skills)
print('Person Info:', person_info)

# declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Aryan', 'Ahmad', 'Pakistan', 22, False

print(first_name, last_name, country, age, is_married)

print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('Age:', age)
print('Is Married:', is_married)