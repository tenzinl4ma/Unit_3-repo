import random

class Seat:
    def __init__(self, type: str, seat_no: str, car_no: int, occupied: bool = None):
        self.occupied = random.randint(0, 1) if occupied is None else occupied
        self.type = type
        self.seat_no = seat_no
        self.car_no = car_no

    def __repr__(self):
        return f"< {self.info()} >"
        
    def is_taken(self):
        return self.occupied

    def get_price(self, base: int):
        categories = {
            "reserved": 1.1,
            "non-reserved": 1.0,
            "green": 1.25,
            "grand": 1.35
        }
        return int(base * categories.get(self.type, 1.0))

    def info(self) -> str:
        return f"Seat {self.seat_no} is in car {self.car_no} and it is {'occupied' if self.occupied else 'free'}"

# Creating a Shinkansen
cars = [
    ('grand', 20), ('green', 30), ('green', 30), ('reserved', 100),
    ('reserved', 100), ('reserved', 100), ('reserved', 100),
    ('non-reserved', 100), ('non-reserved', 100), ('non-reserved', 100)
]

shinkansen = []

for i, c in enumerate(cars):
    car_type, num_seats = c
    current_car = {'class': car_type, 'number': i + 1, "seats": []}
    
    for col in "ABCDE":
        for row in range(1, num_seats // 5 + 1):
            seat_no = f"{row}{col}"
            s = Seat(type=car_type, seat_no=seat_no, car_no=i + 1)
            current_car['seats'].append(s)
    
    shinkansen.append(current_car)

for car in shinkansen:
    print(f"Car {car['number']} ({car['class']}): {len(car['seats'])} seats")
