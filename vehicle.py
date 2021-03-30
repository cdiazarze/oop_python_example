from abc import ABC, abstractmethod
from interface import implements
from machine import Machine
from i_move import IMove

class Vehicle(Machine, IMove, ABC):

    GASOLINE_USE = 30

    def __init__(
        self, model, gasoline, passengers
    ):
        super(Vehicle, self).__init__(model, gasoline)
        self.passengers = passengers

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        if value < 0:
            self.__passengers = 0
        else:
            self.__passengers = value

    # @abstractmethod
    # def move(self):
    #     pass

    def __str__(self):
        return f'Vehicle {self.model}'