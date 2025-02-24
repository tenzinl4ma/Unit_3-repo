# Question


<img width="1006" alt="Screenshot 2025-02-24 at 2 05 14 PM" src="https://github.com/user-attachments/assets/43b123da-72bb-43a3-811f-6fa6258c51f8" />


# Code 
```.py
class palNum:
    def __init__(self, A:int, B:int):
        self.A = A
        self.B = B
    def get_pal_list(self):
        output = []
        for n in range(self.A, (self.B + 1)):
            a = ""
            for let in str(n):
                a = let + a
            if str(n) == a:
                output.append(n)
        return output

test = palNum(1, 9)
print(test.get_pal_list())

test = palNum(10, 199)
print(test.get_pal_list())

```
## Evidence 
<img width="1462" alt="Screenshot 2025-02-24 at 8 06 09 PM" src="https://github.com/user-attachments/assets/11a18d8d-b934-4f55-9d72-023e2422fd3a" />
## UML Diagram

![Screenshot 2025-02-24 at 8 08 05 PM](https://github.com/user-attachments/assets/9390f70e-bfbc-469c-b9f7-23af9a9d42f5)
