# Question
<img width="1020" alt="Screenshot 2025-02-24 at 2 10 55 PM" src="https://github.com/user-attachments/assets/d19d34c6-bac7-480f-8962-c6417faa933b" />




# Code 

```.python
class CalorieCount:
    def __init__(self, daily_limit: int):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def add_meal(self, cal: int, pro: int, car: int, fat: int):
        self.daily_intake += cal
        self.protein += pro
        self.carbs += car
        self.fat += fat

    def get_protein_percentage(self) -> float:
        if self.daily_intake == 0:
            return 0  # Avoid division by zero
        return (4 * self.protein) / self.daily_intake

    def on_track(self) -> bool:
        return self.daily_intake <= self.daily_limit


# **Example Usage:**
sunday = CalorieCount(1500)

sunday.add_meal(716, 38, 38, 45)
sunday.add_meal(230, 16, 8, 16)
sunday.add_meal(568, 38, 50, 24)

print(sunday.on_track())  # Expected Output: False
print(sunday.get_protein_percentage())  # Expected Output: 0.24


```



# Evidence

<img width="1022" alt="Screenshot 2025-02-24 at 8 51 04 PM" src="https://github.com/user-attachments/assets/8272fa06-e986-4306-87ae-33c425f28687" />

# UML Diagram

![Screenshot 2025-02-24 at 8 55 20 PM](https://github.com/user-attachments/assets/d1cf7c74-6a06-4a9f-a3af-39622b147a2b)


