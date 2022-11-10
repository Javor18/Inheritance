class Vehicle:

    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __int__(self, fuel, horse_power):

        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):

        if self.fuel_consumption * kilometers <= self.fuel:

            self.fuel -= self.fuel_consumption * kilometers


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)