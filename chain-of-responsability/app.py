from buget import Buget
from item import Item
from calc_discount import Calc_Discount

buget = Buget()
buget.add_item(Item('Xbox One', 2800))
buget.add_item(Item('PlayStation 3', 2700))
buget.add_item(Item('PC Gamer', 2600))

print("value:", buget.value)

calc_discount = Calc_Discount()
print("with discount:", calc_discount.calculate(buget))



