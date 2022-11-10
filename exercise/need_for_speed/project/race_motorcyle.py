from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION = 8

    def __int__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)