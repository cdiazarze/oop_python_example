from vehicle import Vehicle

class Plane(Vehicle):

    LOW_GASOLINE_LEVEL = 50

    def __init__(self, id, model, gasoline, passengers):
        super(Plane, self).__init__(model, gasoline, passengers)
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def dispatch_alarm(self, message):
        print(f'Plane {self.id}:\t{message} alarm!')

    def dispatch_level(self, message):
        print(f'Plane {self.id}:\t{message}')

    def move(self):
        print (f'Plane {self.id}:\tFlying')
        self.gasoline_level -= self.GASOLINE_USE

    def __str__(self):
        return f'Plane {self.id}'







