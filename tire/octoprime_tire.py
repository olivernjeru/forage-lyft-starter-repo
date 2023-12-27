from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor_data, sum):
        self.sensor_data = sensor_data
        self.sum = sum

    def needs_service(self):
        for data in self.sensor_data:
            sum += self.sensor_data[data]

        if self.sum >= 3:
            return True
        else:
            return False
