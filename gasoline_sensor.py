from sensor import Sensor

class GasolineSensor(Sensor):

    OBJECTIVE = 'Gasoline'
    DEFAULT_KEY = 'gasoline_level'
    DEFAULT_LOW_LEVEL_CRITERIA = 'LOW_GASOLINE_LEVEL'

    def __init__(self, machine):
        super(GasolineSensor, self).__init__(
            machine, self.OBJECTIVE,
            self.DEFAULT_KEY, self.DEFAULT_LOW_LEVEL_CRITERIA
        )
    
    def check_level(self):
        super().check_level()