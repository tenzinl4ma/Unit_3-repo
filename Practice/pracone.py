import random

class HotelReservation:
    def __init__(self, name: str, age: int, phone_no: int, email: str, room_type: str):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.email = email
        self.room_type = room_type  # e.g., "vip", "vvip", "regular"
        self.id = random.randint(1, 100)  # Generate a random ID between 1 and 100

    def __str__(self):
        return (f"Reservation Details:\n"
                f"Name: {self.name}\n"
                f"ID: {self.id}\n"
                f"Age: {self.age}\n"
                f"Phone Number: {self.phone_no}\n"
                f"Email: {self.email}\n"
                f"Room Type: {self.room_type}")

# Example of creating a reservation
reserver = HotelReservation("Tenzin", 10, 123204, "fjsdahffja@gmail.com", "vip")
print(reserver)
