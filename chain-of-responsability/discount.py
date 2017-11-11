class Discount_By_Value():
	def __init__(self, next_discount):
		self.__next_discount = next_discount

	def calculate(self, buget):
		if buget.value >= 500:
			return buget.value * 0.1
		else:
			return self.__next_discount.calculate(buget)

class Discount_By_Items():
	def __init__(self, next_discount):
		self.__next_discount = next_discount

	def calculate(self, buget):
		if buget.total_itens >= 5:
			return buget.value * 0.05
		else:
			return self.__next_discount.calculate(buget)

class No_Discount():
	def calculate(self, buget):
		return 0	

