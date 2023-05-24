from engine import EngineInterface

class SternmanEngine(EngineInterface):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if(self.warning_light_on):
            return True
        else:
            return False
        
