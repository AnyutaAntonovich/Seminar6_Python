# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list1 = [random.randint(-50, 50) for i in range(random.randint(10, 50))]
list2 = []
print(*list1)

max_i = int(input('Input the value MAX = '))
min_i = int(input('Input the value MIN = '))

if max_i >= min_i:
   for i in range(len(list1)):
      if max_i >= list1[i] and min_i <= list1[i]:
          list2.append(i)
   print('Indexes: ', list2)
   print('Quantity: ', len(list2))
