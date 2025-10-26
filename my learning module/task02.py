import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number= registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


        # question 2
    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

        # question 3
    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours

        # question 4

    def __str__(self):
        return f"{self.registration_number:10} | {self.maximum_speed:13} | {self.current_speed:13} | {self.travelled_distance:17.1f}"

    # for question 1:  The main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
car1 = Car('ABC-123)', 142)
print('registration | maximum_speed (km/h) | current_speed | travelled_distance(km)')
print('_' * 65)
print(car1)

    #for question 2: Testing the speed of the car ( Acceleration method)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f'\nCurrent speed after accelerations: {car1.current_speed} km/h')

car1.accelerate(-200)
print(f'Final speed after emergency brake: {car1.current_speed} km/h')


     # for question 3 : drive test
car1.current_speed = 60
car1.travelled_distance = 2000
car1.drive(1.5)
print(f"\nTravelled distance after 1.5 hours: {car1.travelled_distance} km")

     # question 4: car race
cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))

race_ongoing  = True
number_of_hours = 0

while race_ongoing:
    number_of_hours += 1
    for car in cars:
        change_speed = random.randint(-10, 15)
        car.accelerate(change_speed)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_ongoing = False

           # final result
print('\n Race finished! Result after', number_of_hours, 'hours')
print('Registration | Max Speed (km/h) | Current Speed | Travelled Distance(km')
print('_' * 70)
for car in cars:
    print(car)