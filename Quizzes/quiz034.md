
# Python Code
```.py
import random

class Seat:
    def __init__(self, seat_no: str, type: str, occupied: bool = None):
        self.seat_no = seat_no
        self.type = type
        self.occupied = occupied

    def __str__(self):
        status = "Occupied" if self.occupied else "Available"
        return f"Seat {self.seat_no}: {self.type}, {status}"

    def is_occupied(self):
        return self.occupied

    def set_occupied(self, is_occupied: bool):
        self.occupied = is_occupied


seat1 = Seat("1A", "window")
seat2 = Seat("2B", "aisle", True)
seat3 = Seat("2C", "window", True)

print(seat1)
print(seat2)
print(seat3)
'''
### Proof of Work

<img width="773" alt="Screenshot 2025-02-05 at 11 07 15 AM" src="https://github.com/user-attachments/assets/ca66580a-c339-4277-ac27-1c4214cefdad" />
