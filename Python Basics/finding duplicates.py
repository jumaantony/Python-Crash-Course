# some_list = ['a', 'b', 'c', 'd', 'a', 'b', 'n', 'n']
some_list = "six sixty seven"
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)