# print("Data Structures")

# my_list = list()
# my_second_list = [4+5j,'ana are mere',-20.65,True,None ]

# print(len(my_second_list))
# print(my_second_list[3])
# print('index 3:', my_second_list[3])

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list)
# copied_list = my_list[0::2]
# print (copied_list)
# my_sliced_list = my_list[4:]
# my_sliced_list2 = my_list[:4]
# print(my_sliced_list)
# print(my_sliced_list2)

my_list_string = ['ana', 'are', 'mere', "si", "e", "incantata"]
my_list_string.append('Meh')
my_list_string.remove("si")
print(my_list_string)
# my_list_string = ['ana', 'are', 'mere', "si", "e", "incantata"]
# my_list_string.sort()
# my_sorted_list = sorted(my_list_string)
# print(my_sorted_list)

# elements = []
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_1.extend(list_2)
# print(list_1)

# my_list = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# my_tuple = (1, 2, 3, 1, 2, 3, 1, 2, 3)

# print (my_list, my_list.__sizeof__())
# print(my_tuple, my_tuple.__sizeof__())


# my_dictionary = dict()
#
# my_dictionary1 = {
#     "key_1": 12,
#     "key_2": 4 + 5j,
#     3: True,
#     4: None,
#     5 + 2j: "",
#     ("key6"): [1, 3, 4],
#     -8: ('first', 'second', 'third')
# }
#
# person_1 = {
#     'first name': "ion",
#     'last name': 'popescu',
#     'age': '20',
#     'preferinte': {
#         1: "fotbal",
#         2: "tenis",
#         3: "baschet"
#     }
# }
#
# person_2 = dict(person_1)
#
# person_2['first name'] = "vasile"
# print(person_1)
# print(person_2)

# print(person['first name'])
##print(person.get('email', 'Cheia nu a fost gasita'))
# print(person.values())
# for value in person.values():
# print (value)

# for key, value in person.items():
# print(f"{key} -> {value}")

# for preferinte in person.get('preferinte').values():
#     print(preferinte)

# list_1 = [1, 2, 3]
# list_2 = list_1
#
# print(list_2)
# list_1.append(4)
# print(list_2)

#
# my_set = { "item", 2, 3+4j, True, None}
# my_set_2 = { 1, "true", "yes", 23, 2}
#
# my_set.update(my_set_2)
# print(my_set)

# my_list = [1, 2, 3, 4, 4, 4 ,5 ,6 ,7, 7, 8]
# unique_ids = []
# for el in my_list:
#     if el not in unique_ids:
#         unique_ids.append(el)
# print(my_list)
# print(unique_ids)
#
# unique_set_ids = set(my_list)
# print(unique_set_ids)
#
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 3, 6 , 7}
# s3 = {3, 2}
# s1.intersection(s2)
#
# print(s1.issuperset(s2))
# print(s3.issubset(s1))


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a_set = set(a)
b_set = set(b)

elemente_comune = a_set.intersection(b_set)
print(elemente_comune)





