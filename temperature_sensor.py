from sensor import Sensor

class TemperatureSensor(Sensor):

    OBJECTIVE = 'Temperature'
    DEFAULT_KEY = 'temperature_level'
    DEFAULT_HIGH_LEVEL_CRITERIA = 'HIGH_TEMPERATURE_LEVEL'

    def __init__(self, machine):
        super(TemperatureSensor, self).__init__(
            machine, self.OBJECTIVE,
            self.DEFAULT_KEY, self.DEFAULT_HIGH_LEVEL_CRITERIA
        )

    def check_level(self):
        if (
            getattr(self.machine, self.key) >
            getattr(self.machine, self.criteria)
        ):
            self.dispatch_alarm()
        else:
            self.get_level()

        