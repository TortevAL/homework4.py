immutable_var = 1, 'aple', False, 45
print(immutable_var)
#immutable_var[2]= True          #объект 'tuple' не поддерживает назначение элементов
mutable_lis = ([1, 'aple', False], 45)
print(mutable_lis)
mutable_lis[0][2] = True
print(mutable_lis)