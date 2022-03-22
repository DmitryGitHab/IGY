'''1 задание'''

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator(list):

    def __init__(self, list_incoming):
        self.list_incoming = list_incoming
        self.result = []

    def __iter__(self):
        for list_ in self.list_incoming:
            for item_ in list_:
                self.result.append(item_)
        return self

    def __next__(self):
        if len(self.result) > 0:
            return self.result.pop(0)
        else:
            raise StopIteration


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print('*'*33, 'Завершено задание №1')
'''2 задание'''

def flat_generator(lists):
    for list_ in lists:
        for item in list_:
            yield item


for item in flat_generator(nested_list):
	print(item)


print('*'*33, 'Завершено задание №2')

'''3 задание'''


nested_list = [
    ['a', 'b', [1, 2, None], 'c'],
    ['d', 'e', [1, 2, [1, 2, None], None], 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator(list):

	def __init__(self, list_incoming):
		self.list_incoming = list_incoming
		self.result = []

	def list_unpacking(self, list_):
		for item in list_:
			if type(item) is list:
				self.list_unpacking(item)
			else:
				self.result.append(item)

	def __iter__(self):
		self.list_unpacking(self.list_incoming)
		return self

	def __next__(self):
		if len(self.result) > 0:
			return self.result.pop(0)
		else:
			raise StopIteration


for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print('*'*33,  'Завершено задание №3')

