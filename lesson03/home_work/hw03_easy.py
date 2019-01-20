# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    number = str(number).split('.')     # Делим строку по точке
    number_round = int(number[1])       # Округляемое число
    lenght = len(str(number[1]))        # Длина округляемого числа

    for i in range(1, lenght+1):
        digits_number = number_round % 10
        number_round = int(number_round / 10)

        if i == lenght:
            return (int(number[0])+1)           # В том случае если одни 9

        if number_round%10 == 9:                # Если следующее число 9 пропускаем
            continue

        if digits_number > 6:
            number_round = number_round + 1

        if i >= lenght - ndigits:             # Проверяем до этого ли числа мы округляем
            return '{}.{}'.format(number[0],number_round)
            break


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_number = list(str(ticket_number))
    ticket_number = list(map(int,ticket_number))
    lenght = int(len(ticket_number))
    if lenght != 6:
        return 'Неверный номер билета'
    return 'Вы счастливчик' if sum(ticket_number[0:3]) == sum(ticket_number[3:6])  else 'Увы'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
