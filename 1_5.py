"""
Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.

P.S. На экран в программе ничего выводить не нужно.
"""
class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)

"""
Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), а третий необязательный аргумент - цвет точки (локальное свойство color). Если цвет не указывается, то он по умолчанию принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points укажите цвет 'yellow'.

P.S. На экран в программе ничего выводить не нужно.
"""
class Point:
    def __init__(self, x,y, color='black'):
        self.color = color
        self.y = y
        self.x = x

points = []
for x in list(range(2000))[::2]:
    points.append(Point(x+1,x+1))
points[1].color = 'yellow'

"""
Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
"""
from random import choice, randint
choice
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b) #(верхний правый угол)
        self.ep = (c, d) #(нижний левый)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b) #(верхний правый угол)
        self.ep = (c, d) #(нижний левый)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b) #(верхний правый угол)
        self.ep = (c, d) #(нижний левый)

elements = []
# [elements.append(Line(1,2,3,4)) for _ in range(217)]

figure_classes = [Line, Rect, Ellipse]

elements = [choice(figure_classes)(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)) for _ in range(217)]



for x in elements:
    if isinstance(x, Line):
        #setattr(x, 'sp', (0, 0))
        x.sp = (0,0)
        x.ep = (0,0)



"""
Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
"""

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        for x in (self.a, self.b, self.c):

            if type(x) not in (int, float):
                return 1

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1

        if self.a < (self.b + self.c) and self.b < (self.a + self.c) and self.c < (self.a + self.b):
            return 3

        return 2


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

"""
Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:

gr_1 = Graph(data)
где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса должны формироваться следующие локальные свойства:

data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);

В этом классе объявите следующие методы:

set_data(self, data) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.

Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение:

"Отображение данных закрыто"

Прочитайте из входного потока числовые данные с помощью команды:

data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show() со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться две соответствующие строки.
"""
def list_to_string(list):
    return " ".join(str(a) for a in list)

class Graph:
    is_show  = True

    def __init__(self, data):
        self.data = data.copy()

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        print(list_to_string(self.data)) if self.is_show else print("Отображение данных закрыто")

    def show_graph(self):
        print(f"Графическое отображение данных: {list_to_string(self.data)}") if self.is_show else print("Отображение данных закрыто")

    def show_bar(self):
        print(f"Столбчатая диаграмма: {list_to_string(self.data)}") if self.is_show else print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show

data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()