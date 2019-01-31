# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


# class treugolnik(object):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#         def dlina_storoni(k1,k2):
#             return math.sqrt((k1[0] - k2[0]) ** 2 + (k1[1] - k2[1]) ** 2)
#
#         self.ab = dlina_storoni(self.a,self.b)
#         self.bc = dlina_storoni(self.b,self.c)
#         self.ca = dlina_storoni(self.c,self.a)
#
#     def perimetr(self):
#         return self.ab + self.bc + self.ca
#
#     def visota_treug(self):
#         p = self.ploshad()
#         return 2 * p / self.ab
#
#     def ploshad(self):
#         p = self.perimetr()/2
#         return math.sqrt(p*(p - self.ab) * (p - self.bc) * (p - self.ca))
#
#
# a = treugolnik((4, 3), (-2, 1), (3, -4))
#
#
# print(a.ploshad())
# print(a.perimetr())
# print(a.visota_treug())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class ravnobochnaya_trapecia(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        def dlina_storoni(k1,k2):
            return math.sqrt((k1[0] - k2[0]) ** 2 + (k1[1] - k2[1]) ** 2)

        self.ab = dlina_storoni(self.a,self.b)
        self.bc = dlina_storoni(self.b,self.c)
        self.cd = dlina_storoni(self.c,self.d)
        self.da = dlina_storoni(self.d,self.a)

    def proverka(self):

        c = math.sqrt(((self.b[0] - self.a[0]) ** 2) + ((self.b[1] - self.a[1]) ** 2))
        d = math.sqrt(((self.d[0] - self.c[0]) ** 2) + ((self.d[1] - self.c[1]) ** 2))

        if c == d:
            return "Трапеция равнобокая"
        else:
            return "Трапеция неравнобокая"

    def perimemtr(self):
        return  self.ab + self.bc + self.cd + self.da

    def ploshad(self):
        h = math.sqrt(self.cd**2 - ((self.ab - self.bc)/4))
        s = ((self.ab + self.bc)/2)*h

        return s


b = ravnobochnaya_trapecia ((0,0),(3,3),(6,3),(9,0))

print('A', b.ab,'B', b.bc,'C', b.cd,'D', b.da)
print(b.proverka())
print(b.perimemtr())
print(b.ploshad())