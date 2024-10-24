immutable_var = (1, 2, "123", [1, 2,])
print(immutable_var)

#immutable_var[0] = 1  #Возникнет ошибка, т.к. кортеж является неизменяемой коллекцией

mutable_list = [1, 2, "123"]
print(mutable_list)

mutable_list[0] = 12
mutable_list.append([1, 2])
print('Изменённый список\n', mutable_list, sep='')
