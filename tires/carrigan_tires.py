from tires_interface import TiresInterface

class CarriganTires(TiresInterface):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors
        
    def needs_service(self):
        sum = 0
        for sensor in self.tire_wear_sensors:
            sum = sum + sensor
        return sum >= 3