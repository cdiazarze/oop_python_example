from abc import ABC, abstractmethod

class Machine(ABC):

    LOW_GASOLINE_LEVEL = 30
    HIGH_TEMPERATURE_LEVEL = 100
    DEFAULT_TEMPERATURE = 50

    def __init__(self, model, gasoline):
        self.model = model
        self.gasoline_level = gasoline
        self.temperature_level = self.DEFAULT_TEMPERATURE

    @abstractmethod
    def dispatch_alarm(self, message):
        pass

    @abstractmethod
    def dispatch_level(self, message):
        pass

    def __str__(self):
        return f'Machine: {self.model}'

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def gasoline_level(self):
        return self.__gasoline_level

    @gasoline_level.setter
    def gasoline_level(self, value):
        if value < 0:
            self.__gasoline_level = 0
        elif value < 100:
            self.__gasoline_level = value
        else:
            self.__gasoline_level = 100

    @property
    def temperature_level(self):
        return self.__temperature_level

    @temperature_level.setter
    def temperature_level(self, value):
        self.__temperature_level = value
