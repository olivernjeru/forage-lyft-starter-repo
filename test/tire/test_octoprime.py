import unittest


from tire.octoprime_tire import OctoprimeTire



class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_data = [0.9, 0.8, 0.9, 0.6]

        tire = OctoprimeTire(sensor_data)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_data = [0.2, 0.5, 0.8, 0.3]

        tire = OctoprimeTire(sensor_data)
        self.assertFalse(tire.needs_service())
