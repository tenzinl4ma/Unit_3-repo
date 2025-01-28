class Car:
    carstarted = 0  # Class variable to track the number of times the car has started

    def __init__(self, start, brake, acceleration, fuel):
        self.start = start
        self.brake = brake
        self.acceleration = acceleration
        self.fuel = fuel
    
    def moving(self):
        print("The engine has started")
        Car.carstarted += 1  # Increment the class variable each time the car starts

    def speed(self):
        print("The car has accelerated")
    
    def stop(self):
        print("The car has stopped")
    
    def fuel_info(self):
        if Car.carstarted > 2:  # Reference the class variable properly
            print("The car is on low fuel")
        else:
            print("The fuel is good")


car1 = Car("on", "stop","speed","full")
while True:
    us = input('type the command').lower()
    if us == "moving":
        car1.moving()
    if us == "stop":
        car1.stop()
    if us == "speed":
        car1.acceleration()
    