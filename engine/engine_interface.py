from abc import ABC, abstractmethod

class EngineInterface(ABC):
	@abstractmethod
	def needs_service(self):
		pass
