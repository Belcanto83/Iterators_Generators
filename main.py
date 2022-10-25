# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class FlatList:
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

        # if not isinstance(itm, list):
        #     self.current_index += 1
        #     return itm
        # else:
        #     inner_list = iter(itm)
        #     # self.list_iterator = inner_list
        #     # self.__next__ = inner_list.__next__
        #     return next(inner_list)

        # except StopIteration:
        #     itm = next(self.list_iterator)
        #     if isinstance(itm, list):
        #         iter_obj = iter(itm)
        #         return next(iter_obj)


def flatten(s):
    if not s:
        return s
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])


if __name__ == '__main__':
    input_list = [
        ['a', 'b', 'c', 'd', 'J', 4],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    # input_list = [[1, 2, 3], 'b']

    # for item in FlatList(input_list):
    #     print(item)

    res = list(FlatList(input_list))
    print(res)
    print('*' * 100)

    print(flatten(input_list))
