
names = ["ninos", "nahrain", "matthew"]

print(names)  # ['ninos', 'nahrain', 'matthew']

print(names[1]) # nahrain

names[0] = "Ninoos"
print(names[0])  # Ninoos

names.append("daniel")
print(names)   # ['Ninoos', 'nahrain', 'matthew', 'daniel']


# extend a new list(add new list to old list)
old_list = ["a", "b", "c"]
new_list = ["d", "e", "f"]

old_list.extend(new_list)
print(old_list)  # ['a', 'b', 'c', 'd', 'e', 'f']

map = [old_list, new_list]
print(map)  # [['a', 'b', 'c', 'd', 'e', 'f'], ['d', 'e', 'f']]