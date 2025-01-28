# Python Code
```.py
class CompoundInterest:
    def __init__(self, principal: float, rate: float, years:int):
        self.principal= principal
        self.rate = rate
        self.years = years
        
    def calculate(self):
        return self.principal * (1+ self.rate)** self.years
        
### I can use the class on different file by simply import 
### from quiz033.py import CompoundIntest
#### on the same file

test1 = CompoundInterest(100.0, 12.0, 2)
print(f"Compound Interest after {test1.years} years: {test1.calculate():.2f}")
test2 = CompoundInterest(210.0, 20.0, 3)
print(f"Compound Interest after {test2.years} years: {test2.calculate():.2f}")

```