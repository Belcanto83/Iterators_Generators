# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Простой итератор по списку списков (1 уровень вложенности)
class FlatListSimpleIterator:
    def __init__(self, nested_list):
        self.nested_list = iter(nested_list)
        self.initial_length = len(nested_list)
        self.current_index = 0

    def __iter__(self):
        self.list_iterator = iter([])
        return self

    def __next__(self):
        if self.current_index > self.initial_length:
            raise StopIteration

        try:
            itm = next(self.list_iterator)
        except StopIteration:
            self.current_index += 1
            inner_list = next(self.nested_list)
            self.list_iterator = iter(inner_list)
            itm = next(self.list_iterator)
        return itm


# Рекурсивная функция, которая "распрямляет" произвольный список с ЛЮБЫМ уровнем вложенности
def flatten(s):
    if not s:
        return s
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])


# Продвинутый "итератор" (в кавычках), который "распрямляет" произвольный список с ЛЮБЫМ уровнем вложенности
# "Итератор" построен на базе рекурсивной функции "flatten(s)"  (см. выше)
class FlatListAdvanced:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        def flat(s):
            if not s:
                return s
            if isinstance(s[0], list):
                return flat(s[0]) + flat(s[1:])
            return s[:1] + flat(s[1:])

        self.flat_list = iter(flat(self.nested_list))
        return self

    def __next__(self):
        item = next(self.flat_list)
        return item


# Продвинутый итератор, который "распрямляет" произвольный список с ЛЮБЫМ уровнем вложенности
# Итератор распрямляет список, последовательно забирая из него по 1 элементу
# Каждый элемент списка распрямляется рекурсивным методом класса: "get_value"
class NestedIterator:
    def __init__(self, nested_list):
        self.nested_list = iter(nested_list)
        self.nested_item = [next(self.nested_list)]
        self.flat_item = []
        self.get_value(self.nested_item)
        self.flat_item_iterator = iter(self.flat_item)

    def get_value(self, nested_list):
        for itm in nested_list:
            if not isinstance(itm, list):
                self.flat_item.append(itm)
            else:
                self.get_value(itm)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.flat_item_iterator)
        except StopIteration:
            self.nested_item = [next(self.nested_list)]
            self.flat_item = []
            self.get_value(self.nested_item)
            self.flat_item_iterator = iter(self.flat_item)
            item = next(self.flat_item_iterator)
        return item


# Простой генератор по списку списков (1 уровень вложенности)
def simple_generator(nested_list):
    for itm_group in nested_list:
        yield from itm_group
        # for itm in itm_group:
        #     yield itm


def simple_generator_2(nested_list):
    return (itm for group in nested_list for itm in group)


# Продвинутый генератор по списку, который "распрямляет" произвольный список с ЛЮБЫМ уровнем вложенности
def advanced_generator(nested_list):
    for itm in nested_list:
        if not isinstance(itm, list):
            yield itm
        else:
            yield from advanced_generator(itm)


if __name__ == '__main__':
    input_list_simple = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    input_list_complicated = [
        1, ['b', ['c', 'd']], 'e', 2,
        ['f', ['g', 'h'], ['i', False]],
        [3, 4, None], 5
    ]

    # for elem in NestedIterator(input_list_complicated):
    #     print(elem)
    # print('*' * 100)

    print('Задача 1. Простой итератор по простому списку:')
    print('Простой список:', input_list_simple)
    res = list(FlatListSimpleIterator(input_list_simple))
    print('"Выпрямленный" список:', res)
    print('*' * 100)

    print('Задача 2. Простой генератор по простому списку:')
    print('Простой список:', input_list_simple)
    res = list(simple_generator(input_list_simple))
    print('"Выпрямленный" список:', res)
    print('*' * 100)

    print('Задача 3. Продвинутый (рекурсивный) итератор по сложному списку:')
    print('Сложный список:', input_list_complicated)
    res = list(NestedIterator(input_list_complicated))
    print('"Выпрямленный" список:', res)
    print('*' * 100)

    print('Задача 4. Продвинутый (рекурсивный) генератор по сложному списку:')
    print('Сложный список:', input_list_complicated)
    res = list(advanced_generator(input_list_complicated))
    print('"Выпрямленный" список:', res)
