# Dictionary Comprehensions

# Gross Code
# simple_dict = {
#   'a':1,
#   'b':2
# }

# my_dict = {k:v**2 for k,v in simple_dict.items()}
# print(my_dict)
# {'a': 1, 'b': 4}

# Clean Code
my_dict = {num:num*2 for num in[1,2,3,4,5,6]}
my_dict2 = {num:num*2 for num in[1,2,3,4,5,6] if num % 2 == 0}

print(my_dict) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12}
print(my_dict2) # {2: 4, 4: 8, 6: 12}