class Train:
    count = 0
    def __init__(t, id:str, speed:float):
        t.id = id
        t.speed = speed
        Train.count +=1
        
        
    def info(t):
        return f" Train ID: {t.id} speed : {t.speed} km/h"
    def get_speed(t)->float:
        return t.speed
    def get_count(t)->int:
        return f"The count of train is {Train.count}"
        
shinano = Train(id='local-2', speed = 43.0)
print(shinano.info())

class CargoTrain(Train):
    def __init__(t, id, speed, cargo_capacity:float):
        super().__init__(id= id, speed= speed)
        t.cargo_capacity = cargo_capacity
        def info(t):
            return f"{super().info()}, {t.cargo_capacity} kg"


gunma = CargoTrain(id = 'gunma-07', speed=30.0, cargo_capacity=50.0)
    
print(gunma.get_speed(), gunma.info())
print(Train.count)

class PassengerTrain(CargoTrain):
    def __init__(t, id, speed, passenger_capacity):
        super().__init__(id, speed, cargo_capacity)
        t.cargo_capacity = passenger_capacity
    def info(t):
        return "{super().info(), t.passenger_capacity} kg"
        
        
        
        
        
class Mammal:
    def __init__(self, name:str, age:int, origin:str):
        self.name = name
        self.age = age
        self.origin = origin
        
    def describe(self):
        return f"{self.name.upper()} is a mamal {self.age} years old from {self.origin}"
    
    
    
class Pet:
    def __init__(self, owner_name:str):
        self.owner_name = owner_name
    
    def show_owner(self):
        return f" this pet belongs to {self.owner_name}"
    
    
    
class Dog(Mammal, Pet):
    def __init__(self, name, age, origin, owner_name:str, breed:str):
        Mammal.__init__(self, name = name, age= age, origin="local zoo")
        Pet.__init__(self, owner_name=owner_name)
        self.breed = breed
        
        
        
        def get_breed(self):
            return f" this dog is of breed :{self.breed}"
        
buddy = Dog(name = "lenon", age = 2, owner_name=" Mr.Ray", breed=" golden retriver")
print(buddy.describe())
print(buddy.show_owner())
