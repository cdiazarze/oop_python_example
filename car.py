from vehicle import Vehicle

class Car(Vehicle):

    GASOLINE_USE = 20

    def __init__(self, model, gasoline, passengers):
        super(Car, self).__init__(model, gasoline, passengers)

    def dispatch_alarm(self, message):
        print(f'Car {self.model}:\t{message} alarm!')
    
    def dispatch_level(self, message):
        print(f'Car {self.model}:\t{message}')
    
    def move(self):
        print (f'Car {self.model}:\tDriving')
        self.gasoline_level -= self.GASOLINE_USE

    def __str__(self):
        return f'Car {self.model}'