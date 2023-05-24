from abc import ABC, abstractmethod

class TiresInterface(ABC):
	@abstractmethod
	def needs_service(self):
		pass
