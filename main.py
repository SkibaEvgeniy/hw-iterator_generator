import types

class FlatIterator:
    
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        

    def __iter__(self):
        self.list_ = []
        self.n = -1
        self.iter_ = iter(self.list_)
        for group in self.list_of_list:
            self.list_.extend(group)
        return self

    def __next__(self):
        self.n += 1
        if self.n == len(self.list_):
            raise StopIteration
        item = next(self.iter_)
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
        # print('testing')
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    # print('test 1 - ok')

# -----------------------------------------------

def flat_generator(list_of_lists):
    flat_list = []
    for item in list_of_lists:
        flat_list.extend(item)
    for i in flat_list:
        yield i

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        # print(1)
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    # print(2)
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    # print(3)

if __name__ == '__main__':
    test_1(), test_2()

