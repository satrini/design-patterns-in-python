class Buget():
	def __init__(self):
		self.__items = []

	@property
	def value(self):
		total = 0.0
		for item in self.__items:
			total += item.value

		return total

	def add_item(self, item):
		self.__items.append(item)

	def get_items(self):
		return tuple(self.__items)

	@property
	def total_items(self):
		return len(self.__items)

	