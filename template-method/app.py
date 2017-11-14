from buget import Buget
from item import Item
from calc_discount import Calc_Discount
from taxing import ICMS, ISS, ICV, ICA
from calc_taxing import Calc_Taxing

buget = Buget()
buget.add_item(Item('Xbox One', 2800))
buget.add_item(Item('PlayStation 3', 2700))
buget.add_item(Item('PC Gamer', 2600))

print("value:", buget.value)

calc_discount = Calc_Discount()
calc_taxing = Calc_Taxing()

with_ICMS = calc_taxing.calculate(buget, ICMS())
with_ISS = calc_taxing.calculate(buget, ISS())
with_discount = calc_discount.calculate(buget)

print("ICMS:", with_ICMS)
print("ISS:", with_ISS)
print("discount:", with_discount)
print("total:", buget.value + with_ICMS + with_ISS - with_discount)

print("\n")

print("ICV:", calc_taxing.calculate(buget, ICV()))
print("ICA:", calc_taxing.calculate(buget, ICA()))



