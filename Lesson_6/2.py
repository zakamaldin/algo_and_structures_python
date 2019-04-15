"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

# когда-то делал свою реализацию стэка, можно ли как-то подобным образом поступить с методами класса?
# или питон не хранит в словаре имена и ссылки на методы?

from pympler import asizeof


class MyStack:
    def __init__(self, *args):
        self.items = []
        if args:
            for a in args:
                self.items.insert(0, a)

    def Push(self, *args):
        if args:
            for a in args:
                self.items.insert(0, a)

    def IsStackEmpty(self):
        answer = True
        if self.items:
            answer = False
        return answer

    def Top(self):
        return self.items[0]

    def Show(self):
        print(self.items)

    def Pop(self):
        if self.items:
            return self.items.pop(0)
        else:
            print("Stack is empty!!!")

    def Length(self):
        return len(self.items)

    def InStack(self, i):
        return i in self.items


class MyStackWithSlots:
    __slots__ = 'items'
    def __init__(self, *args):
        self.items = []
        if args:
            for a in args:
                self.items.insert(0, a)

    def Push(self, *args):
        if args:
            for a in args:
                self.items.insert(0, a)

    def IsStackEmpty(self):
        answer = True
        if self.items:
            answer = False
        return answer

    def Top(self):
        return self.items[0]

    def Show(self):
        print(self.items)

    def Pop(self):
        if self.items:
            return self.items.pop(0)
        else:
            print("Stack is empty!!!")

    def Length(self):
        return len(self.items)

    def InStack(self, i):
        return i in self.items


stack = MyStack(12345)
stack_with_slots = MyStackWithSlots(12345)

print(asizeof.asizeof(stack))
print(asizeof.asizeof(stack_with_slots))