from discount import *

class Calc_Discount():
	def calculate(self, buget):
		discount = Discount_By_Value(
			Discount_By_Items(No_Discount())
		).calculate(buget)

		return discount