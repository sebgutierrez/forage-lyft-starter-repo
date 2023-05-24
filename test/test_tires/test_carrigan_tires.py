import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase): 
    def test_needs_service_true(self): # one or more of the values in the tire wear array is greater than or equal to 0.9
        tire_wear_sensors = [0.2,0.9,0.4,0.3]
        carrigan = CarriganTires(tire_wear_sensors)
        self.assertTrue(carrigan.needs_service())

    def test_needs_service_false(self):
        tire_wear_sensors = [0.2,0.8,0.4,0.3]
        carrigan = CarriganTires(tire_wear_sensors)
        self.assertFalse(carrigan.needs_service())