# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.



# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class FIO:
    def __init__(self ,name, patronymic, surname):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname

    def get_FIO(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname


class pupil(FIO):
    def __init__(self, name, patronymic,surname, mom, dad, scool_class):
        FIO.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.scool_class = scool_class


class teacher(FIO):
    def __init__(self, name, patronymic, surname, subject):
        FIO.__init__(self, name, patronymic, surname)
        self.subject = subject

class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {i.subject: i for i in teachers}


if __name__ == '__main__':

    teachers = [teacher('Петр', 'Юрьевич', 'Зуев', 'Литература'),
                teacher('Алексей', 'Петрович', 'Узуев', 'Химия'),
                teacher('Кирилл', 'Юрьевич', 'Рзуев', 'История'),
                teacher('Юрий', 'Петрович', 'Азуев', 'Математика'),
                teacher('Василий', 'Юрьевич', 'Мизуев', 'ОБЖ')]

    Class = [Class_rooms('7 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('6 С', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('5 Б', [teachers[3], teachers[1], teachers[0]])]

    parents = [FIO('Павел', 'Павлович', 'Орехов'),
               FIO('Татьяна', 'Савельевна', 'Орехова'),
               FIO('Виктор', 'Александровна', 'Максимова'),
               FIO('Наталья', 'Александровна', 'Максимова'),
               FIO('Павел', 'Алексеевна', 'Натаньян'),
               FIO('Оксана', 'Сергеевна', 'Натаньян')]

    pupils = [pupil('Игорь', 'Cеменович', 'Орехов', parents[0], parents[1], Class[0]),
                pupil('Ольга', 'Романова', 'Максимова', parents[2], parents[3], Class[1]),
                pupil('Александр', 'Сергеевич', 'Натаньян', parents[4], parents[5], Class[2])]

    print('Список классов в школе: ')
    for f in Class:
        print(f.class_room)

    for f in Class:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in Class[0].teachersdict.values():
            print(teacher.get_FIO())
    for f in Class:
        print("Ученики в классе {}:".format(f.class_room))
        for st in pupils:
            print(st.get_FIO())
