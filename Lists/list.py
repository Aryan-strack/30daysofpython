empty_list = list()
print(len(empty_list))  # 0

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

animal_products = ['milk', 'meat', 'butter', 'yoghurt']

web_tech = ['HTML', 'CSS', 'JavaScript', 'React', 'Redux', 'Node', 'MongoDB']

countries = ['Finland', 'Denmark', 'Sweden', 'Norway', 'Iceland']

print("Fruits:", fruits)
print('Number of fruits:', len(fruits))
print("Vegetables:", vegetables)
print('Number of vegetables:', len(vegetables))
print("Animal Products:", animal_products)
print('Number of animal products:', len(animal_products))
print("Web Technologies:", web_tech)
print('Number of web technologies:', len(web_tech))
print("Countries:", countries)
print('Number of countries:', len(countries))


fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)  # banana
second_fruit = fruits[1]
print(second_fruit)  # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon

last_index = len(fruits) - 1
last_fruit = fruits[last_index]


fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
print(last_fruit)  # lemon
second_last = fruits[-2]
print(second_last)  # orange
third_last = fruits[-3]
print(third_last)  # orange


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
all_fruits = fruits[0:]

orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'  # changing the first item
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'  # changing the second item
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'pineapple'  # changing the last item

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
fruits.append('lime')
print(fruits)


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'watermelon')  # inserting 'watermelon' at index 2
print(fruits)  # ['banana', 'orange', 'watermelon', 'mango', 'lemon']
fruits.list(3, 'kiwi')  # inserting 'kiwi' at index 3
print(fruits)


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')  # remove banana from the list
print(fruits)  # ['orange', 'mango', 'lemon']

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()  # remove the last item in the list

fruits.remove(0)
print(fruits)  # ['banana', 'mango']


fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits) 


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']



postive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + postive_numbers
print(integers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Number:' , num1)  # [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5, -4, -3, -2, -1]
postive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(postive_numbers)
print('Integers:' , negative_numbers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegatables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegatables)
print('Fruits and Vegetables:' , fruits)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('banana'))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3


fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('banana'))  # 0
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())  # ['lemon', 'mango', 'orange', 'banana']


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)  # ['banana', 'lemon', 'mango', 'orange']

fruits.sort(reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24,     