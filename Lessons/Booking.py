class Hotel:
    count = 0
    
    def __init__(self, name: str, location: str, stars: int):
        self.location = location
        self.stars = stars
        self.name = name
        Hotel.count += 1  # Correctly increment the count
    
    def show_name(self):
        return f"Your hotel name is: {self.name}"
    
    def show_address(self):
        return f"The address of the {self.name} is: {self.location}"
    
    def show_star(self):
        if self.stars < 1:
            return f"The hotel has less than 1 star, not good."
        elif self.stars <= 3:
            return f"The hotel is decent, has more than one star, good."
        else:
            return f"The hotel is luxurious, has more than 3 stars, excellent!"

hotel1 = Hotel("ABC", "Karuizawa Prince Shopping Mall", 4)
print(hotel1.show_name())
print(hotel1.show_address())
print(hotel1.show_star())

class User:
    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

class Booking(User):
    def __init__(self, name, email, age, hotel: Hotel):
        super().__init__(name, email, age)
        self.hotel = hotel
    
    def hotel_booking(self):
        return f"Booking successful for {self.name} at {self.hotel.name} located at {self.hotel.location}"

user1 = Booking("Marshallis Guy", "Nelhu@gmail.com", 30, hotel1)
print(user1.hotel_booking())




hotel2 = Hotel("DEF", "OSAKA-450", 4)
user2 = Booking("JoJo the last avatar", "jojo@gmail.com", 50, hotel2)
print(user2.hotel_booking())
