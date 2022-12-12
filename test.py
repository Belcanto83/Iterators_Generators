from itertools import chain


def closure(x):
    x = []

    def local_func():
        # nonlocal x
        x.append(2)
        res = x + 1
        # print(res)
        return res
    return local_func


# my_func = closure(5)
# print(my_func)
# print(my_func())


class FlatIterator:

    def __init__(self, multi_list):

        self.multi_list = multi_list  # список с вложенными списками

    def __iter__(self):
        self.multi_list_iter = iter(self.multi_list)
        self.nested_list = []  # вложенный список с элементами
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if len(self.nested_list) == self.nested_list_cursor:
            self.nested_list = None
            self.nested_list_cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.multi_list_iter)
                #  если  список пустой, то получаем следующий
                #  если списки закончаться, получим stop iteration

        return self.nested_list[self.nested_list_cursor]


class FlatIteratorEasyWay:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        return chain.from_iterable(self.multi_list)


class FlatIteratorV2:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_stack = [iter(self.multi_list)]  # стэк итераторов
        return self

    def __next__(self):
        while self.iterators_stack:  # пока в стеке есть итераторы
            try:
                current_element = next(self.iterators_stack[-1])
                #  пытаемся получить следующий элемент
            except StopIteration:
                self.iterators_stack.pop()
                continue
            if isinstance(current_element, list):
                # если следующий элемент оказался списком, то
                # добавляем его итератор в стек
                self.iterators_stack.append(iter(current_element))
            else:
                # если элемент не список, то просто возвращаем его
                return current_element
        raise StopIteration


input_list_simple = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

input_list_complicated = [
        1, ['b', ['c', 'd']], 'e', 2,
        ['f', ['gdddd', [['h']]], ['i', [False]]],
        [3, 4, None], 5
    ]

print('Задача 3. Продвинутый (рекурсивный) итератор по сложному списку:')
print('Сложный список:', input_list_complicated)
res = list(FlatIteratorV2(input_list_complicated))
print('"Выпрямленный" список:', res)
print('*' * 100)
