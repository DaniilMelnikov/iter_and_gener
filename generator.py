nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, [2, 4, 6], None],
]

def flat_generator(my_list):
    counter = -1
    while counter < len(my_list) - 1:
        counter += 1
        if type(my_list[counter]) == list:
            for item in flat_generator(my_list[counter]):
                yield item
        else:
            yield my_list[counter]

for item in  flat_generator(nested_list):
	print(item)