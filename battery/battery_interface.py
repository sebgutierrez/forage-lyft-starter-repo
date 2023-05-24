from abc import ABC, abstractmethod

class BatteryInterface(ABC):
	@abstractmethod
	def needs_service(self):
		pass
