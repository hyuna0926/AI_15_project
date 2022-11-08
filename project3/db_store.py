import os
import sqlite3


DATABASE_PATH = os.path.join(os.getcwd(), 'book_data.db')

conn = sqlite3.connect(DATABASE_PATH)
cur = conn.cursor()

drop_table = "DROP TABLE IF EXISTS Book;"

create_table = """CREATE TABLE Book (
                    genre TEXT,
                    title VARCHAR(128),
                    price FLOAT,
                    star FLOAT
                    );"""

cur.execute(drop_table)
cur.execute(create_table)

for row in total_book.itertuples():
    cur.execute("""INSERT INTO Book (genre, title, price, star)
         VALUES (?,?,?,?)""",
         (row[1],row[2],row[3],row[4]))

conn.commit()