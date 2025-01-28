from datetime import datetime
import random
from banksysclass import BankCustomer

people = [
    {"name": "Alice Smith", "dob": "1990-01-15", "email": "alice.smith@example.com"},
    {"name": "Bob Johnson", "dob": "1985-05-30", "email": "bob.johnson@example.com"},
    {"name": "Carol Davis", "dob": "1992-11-20", "email": "carol.davis@example.com"},
    {"name": "David Wilson", "dob": "1988-03-10", "email": "david.wilson@example.com"},
    {"name": "Eve Brown", "dob": "1995-08-25", "email": "eve.brown@example.com"},
    {"name": "Frank Harris", "dob": "1993-12-01", "email": "frank.harris@example.com"},
    {"name": "Grace Martinez", "dob": "1989-06-18", "email": "grace.martinez@example.com"},
    {"name": "Hank Garcia", "dob": "1991-04-12", "email": "hank.garcia@example.com"},
    {"name": "Ivy Lee", "dob": "1996-09-09", "email": "ivy.lee@example.com"},
    {"name": "Jack Clark", "dob": "1994-02-28", "email": "jack.clark@example.com"},
]

customers = []
for p in people:
    customer = BankCustomer(name=p["name"], dob=p["dob"], email=p["email"])
    customers.append(customer)

for customer in customers:
    randeposit = random.randint(0, 1000000)
    print(customer.deposit(randeposit))

print("\nCustomer Details:")
for customer in customers:
    print(f"Name: {customer.get_name()}, Account No: {customer.account_no}, Balance: {customer.balance}")
