# =================================
#        Область видимости
# =================================

# Изолируемые области видимости переменных в python создают только функции
# В python есть 4 области видимости:
# 1/ Локальная
# 2/ Объемлющей функции
# 3/ Глобальная (модуля)
# 4/ Встроенная (builtins)

# Поиск переменной происходит поочередно с 1 по 4 область

x = 5  # Глобальная переменная - доступна в любом месте данного модуля (файла)


def outside():
    y = 10  # доступна в теле данной функции + во всех вложенных

    def inside():
        z = 15  # доступна только в теле данной функции
        print('inside x: {}, y: {}, z: {}'.format(x, y, z))

    inside()
    print('outside x: {}, y: {}, z: {}'.format(x, y, 'z недоступна'))


outside()
print('inside x: {}, y: {}, z: {}'.format(x, 'y недоступна', 'z недоступна'))

x = 5


def wrapper():
    def test1():
        x = 10  # локальная переменная x перекрывает видимость глобальной x
        print('test1 x = ', x)

    def test2():
        print('test2 x = ', x)
        # x = 22  #         ^-- ошибка, выше используем переменную объявленную позднее

    def test3():
        global x  # инструкция global - поиск переменной в глобальной области
        # Так же есть инструкция nonlocal -  поиск переменной в объемлющей функции
        print('test3 x = ', x)
        x = 25

    test1()
    test2()
    test3()

wrapper()
print('after wrapper x = ', x)