# 1. 1.Realizati un program care sa gaseasca al doilea cel mai mic numar din lista.
#
# list_1 = [-8, 1, 2, -2, 0] -> ec.: -2
#
# list_2 = [1, 1, 0, 0, 2, -2, -2] -> ex.: 0
#
# list_3 = [1, -1, 0, -9, 4, -5]
#
# list_4 = [1, 4, 0, 23, 6, 34]

# def find_second_smallest(lst):
#     if len(lst) < 2:
#         return None
#
#     smallest = second_smallest = float('inf')
#
#     for num in lst:
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif num < second_smallest and num != smallest:
#             second_smallest = num
#
#     return second_smallest
#
#
# list_1 = [-8, 1, 2, -2, 0]
# list_2 = [1, 1, 0, 0, 2, -2, -2]
# list_3 = [1, -1, 0, -9, 4, -5]
# list_4 = [1, 4, 0, 23, 6, 34]
#
#
# result_1 = find_second_smallest(list_1)
# result_2 = find_second_smallest(list_2)
# result_3 = find_second_smallest(list_3)
# result_4 = find_second_smallest(list_4)
#
#
# print("Pentru list_1:", result_1)
# print("Pentru list_2:", result_2)
# print("Pentru list_3:", result_3)
# print("Pentru list_4:", result_4)



# 2.Realizati un program care sa creeze o lista, concatenand o lista data, cu nr. de la 1 la n
#
# exemplu:
#
# list-var = ['p', 's']
#
# n = 5
#
# result = ['p1', 's1', 'p2', 's2', 'p3', 's3', 'p4', 's4', 'p5', 's5']

# def concatenate_list_with_numbers(base_list, n):
#     result = []
#
#     for i in range(1, n + 1):
#         for item in base_list:
#             result.append(item + str(i))
#
#     return result
#
# # Exemplu
# list_var = ['p', 's']
# n = 5
#
# result = concatenate_list_with_numbers(list_var, n)
# print(result)



# 3. Scrieti un program care sa faca split dupa al n-lea element intr-o lista:
#
# lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#
# n = 3
#
# result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# def split_list_by_n_elements(input_list, n):
#     result = []
#     for i in range(n):
#         sub_list = []
#         for j in range(i, len(input_list), n):
#             sub_list.append(input_list[j])
#         result.append(sub_list)
#     return result
#
#
# lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = 3
#
# result = split_list_by_n_e    lements(lista_start, n)
# print(result)


# 4. Realizati un program care sa sorteze o lista de dictionare folosind functia Lambda.
#
# models = [{'make':'Huawei', 'model':2, 'color':'Black'}, {'make':'Apple', 'model':'14', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]


# models = [{'make':'Huawei', 'model':2, 'color':'Black'},
#           {'make':'Apple', 'model':14, 'color':'Gold'},
#           {'make':'Samsung', 'model': 7, 'color':'Blue'}]
#
# # Sortarea listei de dicționare folosind o funcție lambda pentru a accesa cheia 'model'
# sorted_models = sorted(models, key=lambda x: x['model'])
#
# # Afișarea rezultatului
# for model in sorted_models:
#     print(model)