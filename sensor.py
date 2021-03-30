from abc import ABC, abstractmethod

class Sensor(ABC):

    def __init__(self, machine, objective, key, criteria):
        self.__machine = machine
        self.__objective = objective
        self.__key = key
        self.__criteria = criteria

    @property
    def machine(self):
        return self.__machine

    @property
    def key(self):
        return self.__key

    @property
    def objective(self):
        return self.__objective

    @property
    def criteria(self):
        return self.__criteria

    def get_level(self):
        self.machine.dispatch_level(
            f'{self.objective}: {getattr(self.machine, self.key)}'
        )

    def dispatch_alarm(self):
        self.machine.dispatch_alarm(f'{self.objective}')

    @abstractmethod
    def check_level(self):
        if (
            getattr(self.machine, self.key) <
            getattr(self.machine, self.criteria)
        ):
            self.dispatch_alarm()
        else:
            self.get_level()
