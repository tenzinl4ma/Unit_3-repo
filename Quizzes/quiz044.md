# Question
<img width="980" alt="Screenshot 2025-02-24 at 2 06 23 PM" src="https://github.com/user-attachments/assets/0f87293a-fcc1-4f35-987e-cf57c0728c22" />


## Code
```.py

class rainDrops:
    def pour(n:int) -> str:
        out = ''
        d = {3:'i', 5:'a', 7:'o'}
        for k,v in d.items():
            out += (n%k==0)* (f'Pl{v}ng')
        out += (len(out)==0) * str(n)
        return out

test = rainDrops
print(test.pour(n=28))
print(test.pour(n=30))
print(test.pour(n=34))
```
## Evidence

<img width="1282" alt="Screenshot 2025-02-24 at 8 11 28 PM" src="https://github.com/user-attachments/assets/4f4df8c0-de0e-4384-a5a2-80d3254a34bb" />


### UML Diagram

![IMG_0065](https://github.com/user-attachments/assets/ca4eefa4-e7c7-499f-af79-b2562eb619df)

