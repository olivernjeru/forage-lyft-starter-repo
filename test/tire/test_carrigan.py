import unittest


from tire.carrigan_tire import CarriganTire



class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_data = [0.2, 0.5, 0.9, 0.3]

        tire = CarriganTire(sensor_data)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_data = [0.2, 0.5, 0.8, 0.3]

        tire = CarriganTire(sensor_data)
        self.assertFalse(tire.needs_service())
