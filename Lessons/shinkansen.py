import random
from copy import deepcopy

class Seat:
    occupied_count = 0  # Class-level counter for occupied seats

    def __init__(self, type: str, seat_no: str, car_no: int, occupied: bool = None):
        self.occupied = random.choice([True, False]) if occupied is None else occupied
        self.type = type
        self.seat_no = seat_no
        self.car_no = car_no
        if self.occupied:
            Seat.occupied_count += 1

    def __repr__(self):
        return f"<{self.info()}>"

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
        status = "occupied" if self.occupied else "free"
        return f"Seat {self.seat_no} is in car {self.car_no} ({status})"

# Creating a Shinkansen
cars = [
    ('grand', 20), ('green', 30), ('green', 30),
    ('reserved', 100), ('reserved', 100), ('reserved', 100), ('reserved', 100),
    ('non-reserved', 100), ('non-reserved', 100), ('non-reserved', 100)
]

shinkansen = []
base_price = 5700

for i, c in enumerate(cars):
    car_type, num_seats = c
    current_car = {
        'class': car_type,
        'number': i + 1,
        'seats': []
    }

    for row in range(1, (num_seats // 5) + 1):
        for col in "ABCDE":
            seat_no = f"{row}{col}"
            s = Seat(type=car_type, seat_no=seat_no, car_no=i + 1)
            current_car['seats'].append(s)
    
    shinkansen.append(current_car)

# Calculate ratio and profits
total_occupied = Seat.occupied_count
total_seats = sum(len(car['seats']) for car in shinkansen)
total_free = total_seats - total_occupied

def ratioer(occupied: int, free: int) -> float:
    return occupied / free if free > 0 else float('inf')

total_profit = sum(
    seat.get_price(base_price) for car in shinkansen for seat in car['seats'] if seat.occupied
)

print(f"Total Seats: {total_seats}")
print(f"Occupied Seats: {total_occupied}")
print(f"Free Seats: {total_free}")
print(f"Occupancy Ratio: {ratioer(total_occupied, total_free):.2f}")
print(f"Total Profit: ¥{total_profit}")
