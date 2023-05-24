from tires_interface import TiresInterface

class OctoprimeTires(TiresInterface):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors
        
    def needs_service(self):
        count = 0
        for sensor in self.tire_wear_sensors:
            if sensor >= 0.9:
                count = count + 1
        return count > 0
        