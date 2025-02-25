# Question
<img width="1004" alt="Screenshot 2025-02-24 at 2 04 02 PM" src="https://github.com/user-attachments/assets/260f74e6-466d-471e-bd7b-6969e5ad7373" />
### fig of question of quizz


# Code
```.py
from quizlib import DatabaseManager, check_text


db = DatabaseManager(db_name='/Users/m22-007/Desktop/Unit3_Repo/Quizzes/bitcoin_exchange (1).db')


query = "SELECT * FROM ledger"
result = db.search(query=query, multiple=True)


for n in result:
    pre_hash = f"id {n[0]},sender_id {n[1]},receiver_id {n[2]},amount {n[3]}"
    
    # Corrected function argument order
    if check_text(text=pre_hash, hashed=n[4]):
        print(f"Tx(id={n[0]}) Signature Matches")
    else:
        print(f"Tx(id={n[0]}) Error Signature")


db.close()

```

## Evidence
<img width="1361" alt="Screenshot 2025-02-24 at 7 56 52 PM" src="https://github.com/user-attachments/assets/f6b64c51-49ea-4206-8feb-79947d86bb21" />

## ER Diagram
![Uploading Screenshot 2025-02-24 at 8.01.14 PM.jpeg…]()

