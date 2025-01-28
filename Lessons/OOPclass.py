class Motorcyle:
    def __init__(self, engine:int, tank_size:int):
        self.fuel_level = 0
        self.engine_size = engine
        self.fuel_capacity = tank_size

    def put_fuel(self, qty:int):
        if self.fuel_level +qty > self.fuel_capacity:
            return 'overflow, too much gas'
        self.fuel_level += qty
        return f'The tank is now {self.fuel_level}'
    def get_fuel_level(self):
        return self.fuel_level

