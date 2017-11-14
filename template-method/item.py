class Item():
	def __init__(self, name, value):
		self.__name = name
		self.__value = value

	@property
	def value(self):
		return self.__value

	@property
	def name(self):
		return self.__name

