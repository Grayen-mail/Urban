my_dict = {'Serg': 1972, 'Elena': 1976}
print('Dict:', my_dict)
print('Existing Serg year:', my_dict['Serg'])
print('Non existing Alex year:', my_dict.get('Alex', 'Нет данных'))
my_dict.update({'Alex': 1984})
my_dict['Matvey'] = 2004
print('Deleted Serg:', my_dict.pop('Serg'))
print(my_dict)

my_set = {7, 7, 2, 2, 3, 3, 4, 6, 4, 5}
print('Set:', my_set)
my_set.add('Something')
my_set.add(True)
my_set.discard(5)
print('Modified:', my_set)
