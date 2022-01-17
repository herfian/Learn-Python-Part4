some_list = ['a','b','b','c','d','e','f','f','g','h','h']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates) # ['b', 'f', 'h']