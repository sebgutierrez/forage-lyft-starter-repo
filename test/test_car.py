import unittest
from datetime import datetime

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestCalliope(unittest.TestCase): # every 30,000 miles and every 2 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        calliope = Car(battery,engine)
        self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        calliope = Car(battery,engine)
        self.assertTrue(calliope.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        calliope = Car(battery,engine)
        self.assertTrue(calliope.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        calliope = Car(battery,engine)
        self.assertTrue(calliope.needs_service())

    def test_both_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        calliope = Car(battery,engine)
        self.assertTrue(calliope.needs_service())

    def test_both_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 29999
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        calliope = Car(battery,engine)
        self.assertTrue(calliope.needs_service())

class TestGlissade(unittest.TestCase): # every 60,000 miles and every 2 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        glissade = Car(battery,engine)
        self.assertTrue(glissade.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        glissade = Car(battery,engine)
        self.assertTrue(glissade.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        glissade = Car(battery,engine)
        self.assertTrue(glissade.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        glissade = Car(battery,engine)
        self.assertTrue(glissade.needs_service())

    def test_both_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        glissade = Car(battery,engine)
        self.assertTrue(glissade.needs_service())

    def test_both_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 59999
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(today, last_service_date)
        glissade = Car(battery,engine)
        self.assertTrue(glissade.needs_service())

class TestPalindrome(unittest.TestCase): # when warning light is on and every 2 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(today, last_service_date)
        palindrome = Car(battery,engine)
        self.assertTrue(palindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(today, last_service_date)
        palindrome = Car(battery,engine)
        self.assertTrue(palindrome.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(today, last_service_date)
        palindrome = Car(battery,engine)
        self.assertTrue(palindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(today, last_service_date)
        palindrome = Car(battery,engine)
        self.assertTrue(palindrome.needs_service())

    def test_both_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(today, last_service_date)
        palindrome = Car(battery,engine)
        self.assertTrue(palindrome.needs_service())

    def test_both_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(today, last_service_date)
        palindrome = Car(battery,engine)
        self.assertTrue(palindrome.needs_service())

class TestRorschach(unittest.TestCase): # every 60,000 miles and every 4 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        rorschach = Car(battery,engine)
        self.assertTrue(rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        rorschach = Car(battery,engine)
        self.assertTrue(rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        rorschach = Car(battery,engine)
        self.assertTrue(rorschach.needs_service()) 

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        rorschach = Car(battery,engine)
        self.assertTrue(rorschach.needs_service())

    def test_both_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        rorschach = Car(battery,engine)
        self.assertTrue(rorschach.needs_service()) 

    def test_both_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 59999
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        rorschach = Car(battery,engine)
        self.assertTrue(rorschach.needs_service()) 

class TestThovex(unittest.TestCase): # every 30,000 miles and every 4 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        thovex  = Car(battery,engine)
        self.assertTrue(thovex.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        thovex  = Car(battery,engine)
        self.assertTrue(thovex.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        thovex  = Car(battery,engine)
        self.assertTrue(thovex.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        thovex  = Car(battery,engine)
        self.assertTrue(thovex.needs_service())

    def test_both_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        thovex  = Car(battery,engine)
        self.assertTrue(thovex.needs_service())

    def test_both_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 29999
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(today, last_service_date)
        thovex  = Car(battery,engine)
        self.assertTrue(thovex.needs_service())

if __name__ == '__main__':
    unittest.main()
