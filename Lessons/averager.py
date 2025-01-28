import sqlite3
db_name = "words.sql"
sqlite3.connect(db_name)
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
haiku = """CREATE TABLE if not exists user(
    id INTEGER PRIMARY KEY,
    words VARCHAR(150)
);
"""

cursor.execute(haiku)
connection.commit()

for word in haiku.split():
    table1 =  "INSERT INTO user(words) values ('hello');"
    cursor.execute(table1)
    connection.commit()


get_user = "SELECT * from ;"
result = cursor.execute(get_user).fetchall()
connection.close()

def averager():
    allwords= result
    
    




