shopping_list = ['detergents', 'sugar', 'notebooks', 'stationary', 'others']

shopping_list.extend(['pc', 'PDA'])

print(shopping_list)

print(shopping_list.pop())

shopping_list.remove('sugar')
print(shopping_list)

shopping_list.sort()
print(shopping_list)
print(sorted(shopping_list))

shopping_list.reverse()
print(shopping_list)
print(list(range(1, 100)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Juma'])
print(new_sentence)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(c)
print(other)
print(d)