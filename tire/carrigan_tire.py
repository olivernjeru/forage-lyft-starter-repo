from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def needs_service(self):
        for data in self.sensor_data:
            if self.sensor_data[data] >= 0.9:
                return True
            else:
                return False
