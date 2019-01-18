# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне./

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

list_fruits = ["яблоко", "банан", "киви", "арбуз"]
count = 0
for i in list_fruits:
    count = count + 1
    print("{}.{:>10}".format(count, i))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = [1, 2, 3, 4, 3]
list_2 = [2, 5, 4]

for i in list_1:
    if i in list_2:
        list_1.remove(i)
print(list_1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list = [1, 2, 3, 4, 5, 6, 7, 9, 10]
list_new = []

for i in list:
    if i%2 == 0:
        list_new.append(i/4)
    else:
        list_new.append(i*2)

print(list)
print(list_new)