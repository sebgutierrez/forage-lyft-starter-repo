from battery import BatteryInterface

from datetime import datetime

class SpindlerBattery(BatteryInterface):

    def needs_service(self, last_service_date, current_date):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False