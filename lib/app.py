# # my_list = ['This is a long sentence', 'Word', 'z']
# # my_list.sort(key = len, reverse=True)
# # print(my_list)

# # my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]


# my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

# # We can define a function for the list to sort by the second key

# def sort_tuple(tuple_value):
    
#     print(tuple_value[0])
#     # print(tuple_value[1])
#     # return the key we want to sort by
#     return tuple_value[1]

# my_list.sort(key = sort_tuple)
# print(my_list)
# # => [('Steve', 1), ('John', 2), ('Joe', 3)]

# my_list = [0, 1, 2, 3]
# print(my_list)
# # => [0, 1, 2, 3]

# my_range = range(4)
# print(my_range)
# # => range(0, 4)

my_string = 'Hello world!'
for char in my_string:
    print(char)
print(my_string[0])

