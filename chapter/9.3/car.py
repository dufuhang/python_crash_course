class Car:
    """A Car Class"""
    def __init__(self, make, model, year):
        """init car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def _get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def _read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def _update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")

    def _increment_odometer(self, miles):
        self.odometer_reading += miles

    def _fill_gas_tank(self):
        print(f"Full done!")

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def _describe_battery(self):
        print(f"This car has a {self.battery_size} kWh battery")

    def _get_range(self):
        range = None
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def _fill_gas_tank(self):
        print(f"This car does't have a gas tank!")

my_leaf = ElectricCar('Nissan', 'leaf', 2024)
print(my_leaf._get_descriptive_name())
my_leaf.battery._describe_battery()
my_leaf.battery._get_range()

















