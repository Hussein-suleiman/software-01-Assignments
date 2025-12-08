class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"  Author: {self.author}")
        print(f"  Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"  Chief Editor: {self.chief_editor}")



class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def set_speed(self, speed):
        self.current_speed = min(speed, self.max_speed)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


if __name__ == "__main__":

    print("=== Publications ===")
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck.print_information()
    print()
    compartment_no6.print_information()

    print("\n=== Cars ===")
    e_car = ElectricCar("ABC-15", 180, 52.5)
    g_car = GasolineCar("ACD-123", 165, 32.3)

    # Set speeds
    e_car.set_speed(150)
    g_car.set_speed(140)

    # Drive for 3 hours
    e_car.drive(3)
    g_car.drive(3)

    # Print travelled distances
    print(f"\nElectric car travelled distance: {e_car.travelled_distance} km")
    print(f"Gasoline car travelled distance: {g_car.travelled_distance} km")
