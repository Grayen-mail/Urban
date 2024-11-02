def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b='string')
print_params(c=False)
print_params(3, 5)

values_list = [5, 'list', (1,2,3)]
print_params(*values_list)

values_dict = {'a': 10, 'b': 'dict', 'c': False}
print_params(**values_dict)

values_list_2 = [21, 'str']
print_params(*values_list_2, 10)
