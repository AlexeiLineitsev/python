# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

k = equation[(equation.index('=',0,len(equation)))+1:equation.index('x',0,len(equation))]
b = equation[(equation.index('+',0,len(equation)))+1:len(equation)]
print(k,b)
k = float(k)
b = float(b)
y = (k*x)+b
print(y)



# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

days_ = {'01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четверное', '05': 'Пятое', '06': 'Шестое',
         '07': 'Седьмое',
         '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одинадцатое',
         '12': 'Двенадцатое', '13': 'Тринадцатое', '14': 'Четырнадцатое', '15': 'Пятнадцатое', '16': 'Шестнадцатое',
         '17': 'Семнадцатое', '18': 'Восемьнадцатое', '19': 'Девятнадцатое',
         '20': 'Двадцатое', '21': 'Двадцать первое', '22': 'Двадцать второе', '23': 'Двадцать третье',
         '24': 'Двадцать четвертое', '25': 'Двадцать пятое', '26': 'Двадцать шестое',
         '27': 'Двадцать седьмое', '28': 'Двадцать восьмое', '29': 'Двадцать девятое', '30': 'Тридцатое',
         '31': 'Тридцать первое'}
month_ = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
          '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}

check_date = 0

while check_date == 0:
    input_date = input("Введите дату в формате ДД.ММ.ГГГГ - ").split('.')
    if int(input_date[0]) > 0 and int(input_date[0]) < 32:
        if int(input_date[1]) > 0 and int(input_date[1]) < 13:
            if int(input_date[2]) > 0 and int(input_date[2]) < 9999:
                check_date = 1
                print(days_[input_date[0]], month_[input_date[1]], input_date[2], 'года')
            else:
                print("Не правильно ввели год")
        else:
            print("Не правильно ввели месяц")
    else:
        print("Не правильно ввели день")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3