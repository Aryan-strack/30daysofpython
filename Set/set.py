st = set()

st = {'item1', 'item2', 'item3', 'item4', 'item5'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

len(st)
len(fruits)


st = { 'item1', 'item2', 'item3', 'item4', 'item5'}
print('Does set st contain item3?')
print('item3' in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)


st = { 'item1', 'item2', 'item3', 'item4', 'item5'}
st.add('item6')
print(st)

st = { 'item1', 'item2', 'item3', 'item4', 'item5'}
st.remove('item3')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.discard('banana')
print(fruits)

fruits.update({'apple', 'grapes'})
print(fruits)


fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)


fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits = list(fruits)
print(fruits)


fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion'}
fruits_and_vegetables = fruits.union(vegetables)
print(fruits_and_vegetables)


whole_numbers = {0, 1, 2, 3, 4, 5}
even_numbers = {0, 2, 4, 6, 8}
print(whole_numbers.intersection(even_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

print(python.intersection(dragon))

print(whole_numbers.isdisjoint(even_numbers))
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))
print(whole_numbers.difference(even_numbers))
