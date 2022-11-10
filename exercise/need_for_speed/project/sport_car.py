from project.car import Car

class SportCar(Car):

    DEFAULT_FUEL_CONSUMPTION = 10

    def __int__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)