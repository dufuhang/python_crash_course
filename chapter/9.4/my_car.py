from car import Car

my_new_car = Car('Audi', 'A4', 2024)
print(my_new_car._get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car._read_odometer()


