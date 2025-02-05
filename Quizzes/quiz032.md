# Python Code
```.py
class HumanResourcesDepartment:
    def __init__(self, name, email, nationality, occupation)->str:
        self.name = name
        self.email = email
        self.nationality = nationality
        self.occupation = occupation
        
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def set_nationality(self, nationality):
        self.nationality = nationality

    def greet(self):
        return f"Hello, {self.name}! You look amazing today!"
        
# Testing the class
test1 = HumanResourcesDepartment("Tenzin", "tenzin243134@gmail.com", "Mars", "Wanderer")

print(f"This is before setting\n{test1.get_email() and test1.greet()}")
test1.set_email("somethinng@gmail.com") and test1.set_nationality("Jupiter")
print(f" This is afeter setting\n {test1.get_email() and test1.greet()}")

print(test1.get_email())

```
### Proof of Work
<img width="1276" alt="Screenshot 2025-02-05 at 11 03 29 AM" src="https://github.com/user-attachments/assets/6a7a559e-d862-44a0-ad74-240096d128e8" />

