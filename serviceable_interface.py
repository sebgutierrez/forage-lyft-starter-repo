from abc import ABC, abstractmethod

class ServiceableInterface(ABC):
	@abstractmethod
	def needs_service(self):
		pass
