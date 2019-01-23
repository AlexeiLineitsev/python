# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import  random

lenght = 5
rand_list = [random.randint(0,150) for i in range(lenght)]
rand_list_new = [i**2 for i in rand_list]



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_fruits_1 = ['Абиу', 'Абрикос', 'Авокадо', 'Айва', 'Аки', 'Алиберция']
list_fruits_2 = ['Яблоко', 'Алиберция', 'Авокадо', 'Банан', 'Аки', 'Абрикос']
list_fruits_3 = [i for i in list_fruits_1 if i in list_fruits_2]


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


import  random

lenght = 10
rand_list = [random.randint(-150,150) for i in range(lenght)]
rand_list_new = [i for i in rand_list if (i > 0) and (i%3 == 0) and (i%4 !=0)]


