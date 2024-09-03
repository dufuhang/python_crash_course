"""A class representing a car"""

class Car:
    """A simple attempt to simulate a car """

    def __init__(self, make, model, year):
        """init car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def _get_descriptive_name(self):
        """Return a descriptive name for a format specification"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def _read_odometer(self):
        """Print a message indicating car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def _update_odometer(self, mileage):
        """
        1. Set the odometer to a specified value.
        2. Rejecting the odometer roll back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")

    def _increment_odometer(self, miles):
        """Increase the odometer by the specified value"""
        self.odometer_reading += miles

    def _fill_gas_tank(self):
        print(f"Full done!")

class Battery:
    def __init__(self, battery_size=40):
        """Initialize the battery properties"""
        self.battery_size = battery_size

    def _describe_battery(self):
        """Print a message describing battery's capacity"""
        print(f"This car has a {self.battery_size} kWh battery")

    def _get_range(self):
        """Print a message describing car's mileage"""
        range = None
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """The unique features of simulating Electric car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def _fill_gas_tank(self):
        print(f"This car does't have a gas tank!")











