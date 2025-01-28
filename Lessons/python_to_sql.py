import sqlite3


db_name = "my_data.sql"
sqlite3.connect(db_name)
connection = sqlite3.connect(db_name)
cursor = connection.cursor()


query_create = """CREATE TABLE if not exists user(
    id INTEGER PRIMARY KEY,
    name VARCHAR(150),
    email TEXT not null unique

);
"""
cursor.execute(query_create)
connection.commit()

new_user = "INSERT INTO user(name, email) values ('Alice smil', 'alxyz@gmail.com');"
cursor.execute(query_create)
connection.commit()

get_user = "SELECT * from user;"
result = cursor.execute(get_user).fetchall()
print(result)
connection.close()
