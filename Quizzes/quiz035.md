### quiz35

```.py
class Person:
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
test1= Person("tensin",12)
print(test1.get_age())  
print(f"{Person("Something",41).get_name()}")

### Inheritance it will make all the methods and attribute available to child class

class Student(Person):
    def __init__(self, name, age, grade:str):
        super().__init__(name, age)
        self.grade = grade
    def get_grade(self):
        return self.grade

#### 
        
test2 = Student("Shrekkk", 100, "G11")

print(f"Hello!{test2.get_name()} Even you are {test2.get_age()} years old. You are in {test2.get_grade()}")
```
### Proof Of Work
<img width="1130" alt="Screenshot 2025-02-05 at 11 09 10 AM" src="https://github.com/user-attachments/assets/0575bcf1-5819-468c-951b-14f696bdcfde" />
