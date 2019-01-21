# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_list = [1,1]
    if n <= 0:
        return 'Неверное n'
    if n > m:
        return 'Неверное m'
    if n == 1 and m ==1:
        return fib_list

    for i in range(2,m-1):
       number_f = fib_list[i-2] + fib_list[i-1]
       fib_list.append(number_f)
    fib_list = fib_list[n-1:m-1]
    return fib_list


print(fibonacci(1,1))
print(fibonacci(6,15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):           # Пузырьковый алгоритм сортировки
    lenght = len(origin_list)-1         # Длина списка
    check = 0                           # Переменная для проверки

    while check != lenght:
        check = 0
        for i in range(0, lenght):
            if origin_list[i] > origin_list[i + 1]:             # Сравниваем попарно элементы
                origin_list.insert(i, origin_list.pop(i + 1))   # Если верно условие if  меняем элементы списка местами
            else:
                check = check + 1                               # Когда список будет отсортирован, выполнится условие
                                                                # while, функция вернет сортированный список
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.





# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

xy = [(1, 1), (3, 2), (3, 5), (1, 4)]       #[(5, 3), (4, 1), (2, 3), (1, 1)]

xy.sort()
print(xy)
t = 0.001
ax = 1
ay = 1
bx = 3
by = 2
cx = 3
cy = 5
dx = 1
dy = 4

# если прямые попарно вертикальны
if (((ax == bx) and (cx == dx)) or ((ax == cx) and (bx == dx)) or ((ax == dx) and (bx == cx))
# или угловые коэффициенты попарно равны
        or ((abs((ay - by) / (ax - bx) - (cy - dy) / (cx - dx)) < t))
        or ((abs((ay - cy) / (ax - cx) - (by - dy) / (bx - dx)) < t))
        or ((abs((ay - dy) / (ax - dx) - (by - cy) / (b.x - cx)) < t))):
    print('Это вершины параллелограмма')
else:
    print('Это не вершины параллелограмма')
