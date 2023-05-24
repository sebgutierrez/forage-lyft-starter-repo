import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase): 
    def test_needs_service_true(self): # the sum of all values in the tire wear array is greater than or equal to 3
        tire_wear_sensors = [0.8,0.8,0.8,0.8]
        octoprime = OctoprimeTires(tire_wear_sensors)
        self.assertTrue(octoprime.needs_service())

    def test_needs_service_false(self):
        tire_wear_sensors = [0.7,0.7,0.7,0.7]
        octoprime = OctoprimeTires(tire_wear_sensors)
        self.assertFalse(octoprime.needs_service())