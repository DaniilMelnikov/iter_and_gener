nested_list = [
	['a', 'b', 'c'],
	['d', 'e', [1, 4, 6], 'f'],
	[1, None, [4, 8, 12]]
]
new_list = []
dict = {1:''}
class FlatIterator:
    def __init__(self, list):
        self.list = list
        self.counter = -1

    def __iter__(self):
        if dict[1] == '':
            dict[1] = self.list[-1]
        def open_list(my_list):
            for el in FlatIterator(my_list):
                pass
            itr = iter(new_list)
            return itr
        for _ in range(len(self.list)):
            if dict[1] == self.list[_]:
                return open_list(self.list[_])
            if type(self.list[_]) == list:
                open_list(self.list[_])
            else:
                new_list.append(self.list[_])
        return self

    def __next__(self):
        if self.counter == len(self.list) - 1:
            raise StopIteration
        else:
            self.counter += 1
            return self.list[self.counter]

for item in FlatIterator(nested_list):
	print(item)