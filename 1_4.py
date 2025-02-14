"""
Подвиг 4. Объявите класс с именем MediaPlayer с двумя методами:

open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со значением аргумента file в объекте класса MediaPlayer)
play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")

Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод open() с аргументом "filemedia1" для объекта media1 и "filemedia2" для объекта media2. После этого вызовите через объекты метод play(). При этом, на экране должно отобразиться две строки (без кавычек):

"Воспроизведение filemedia1"
"Воспроизведение filemedia2"
"""
class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()


"""
Подвиг 5. Объявите класс с именем Graph и методами:

set_data(data) - передача набора данных data для последующего отображения (data - список числовых данных);
draw() - отображение данных (в том же порядке, что и в списке data)

и атрибутом:

LIMIT_Y = [0, 10]

Метод set_data() должен формировать локальное свойство data объекта класса Graph. Атрибут data должен ссылаться на переданный в метод список. Метод draw() должен выводить на экран список в виде строки из чисел, разделенных пробелами и принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).

Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и передайте список:

[10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с соответствующим набором чисел, записанных через пробел. Например (вывод без кавычек):

"10 0 2 5 7"
"""

class Graph:
    LIMIT_Y = [0, 10]
    def set_data(self, data):
        self.data = data

    def draw(self):
        '''
        new_list = []
        [new_list.append(x) for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]]
        print(*new_list)
        '''
        a, b = self.LIMIT_Y
        print(*filter(lambda x: a <= x <= b, self.data))
        '''
        res = (x for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1])
        print(*res)
        '''
graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


"""
Подвиг 7. Имеется следующий класс для считывания информации из входного потока:

import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
Которым, затем, можно воспользоваться следующим образом:

sr = StreamReader()
data, result = sr.readlines()
Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:

def create(self, fields, lst_values): ...

который бы на входе получал кортеж FIELDS из названий локальных атрибутов 
(передается в атрибут fields) и список строк lst_in (передается в атрибут lst_values) 
и формировал бы в объекте класса StreamData локальные свойства с именами полей из fields
 и соответствующими значениями из lst_values.

Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. Если число полей и число строк не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.

P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.

Пример входной информации (Sample Input):

10
Питон - основы мастерства
512
"""

import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            # [setattr(self, name, value) for name, value in zip(fields, lst_values)]
            self.__dict__.update(dict(zip(fields, lst_values)))
            return True
        else:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__, result)


