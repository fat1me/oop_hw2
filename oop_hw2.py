class VirtualException(BaseException):
    def __init__(self, _type, _func):
        BaseException(self)

class newClass():
    def printing(self):
        raise VirtualException()

class Author():
    def printing(self):
        print("Автор: Рэй Брэдрбери")
        print("'451 градус по фаренгейту','Вино из одуванчиков','Лето, прощай!','Р - значит ракета','Лед и пламя'")

class Publishing():
    def printing(self):
        print("Издательство: МИФ")
        print("'Мы - это музыка','Мы дали слово','Мы - звездная пыль','Ловушки мышления','Истории старого дерева'")

class Year():
    def printing(self):
        print("Год издания: 2020")
        print("'Лабиринт Фавна','Королева ничего','Столица беглых','Поймать дракона','В объятиях врага'")

array = [Author(), Publishing(), Year()]
for _new in array:
    _new.printing()