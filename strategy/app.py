from taxing import ISS, ICMS
from calc_taxing import Calc_Taxing
from buget import Buget

buget = Buget(500)
taxing = Calc_Taxing()

print("Value:", buget.value)
print("with ICMS:", taxing.calculate(buget, ICMS()) + buget.value)
print("with ISS:", taxing.calculate(buget, ISS()) + buget.value)