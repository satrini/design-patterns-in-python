from abc import ABC, abstractmethod

class Template_Taxing(ABC):
	def calculate(self, buget):
		if self.should_use_max_taxing(buget):
			return self.use_max_taxing(buget)
		else:
			return self.use_min_taxing(buget)

	@abstractmethod
	def should_use_max_taxing(self, buget):
		pass

	@abstractmethod
	def use_max_taxing(self, buget):
		pass

	@abstractmethod
	def use_min_taxing(self, buget):
		pass

class ISS:
	def calculate(self, buget):
		return buget.value * 0.01

class ICMS:
	def calculate(self, buget):
		return buget.value * 0.03

class ICV(Template_Taxing):
	def should_use_max_taxing(self, buget):
		return buget.value > 1000

	def use_max_taxing(self, buget):
		return buget.value * 0.03

	def use_min_taxing(self, buget):
		return buget.value * 0.02

class ICA(Template_Taxing):
	def should_use_max_taxing(self, buget):
		for item in buget.get_items():
			if item.value > 1500:
				return True
		return False 

	def use_max_taxing(self, buget):
		return buget.value * 0.07

	def use_min_taxing(self, buget):
		return buget.value * 0.05
