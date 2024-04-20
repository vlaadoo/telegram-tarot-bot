import sqlite3
from sqlite3 import Error
import time

def sql_connection():
    try:
        con = sqlite3.connect('database.db')
        print("Connection is established: Database is created in memory")
        return con
    except Error:
        print(Error)

def get_random_row():
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM cards ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    con.close()
    return row

def update_card_desc(new_desc, card_id):
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(f"UPDATE cards SET description = '{new_desc}' WHERE id = {card_id}")
    con.commit()
    con.close()
    
def get_card_name(card_id):
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT title FROM cards WHERE id = {card_id}")
    row = cursor.fetchone()
    con.close()
    return row[0]

def get_card_desc(card_id):
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT title, description FROM cards WHERE id = {card_id}")
    row = cursor.fetchone()
    con.close()
    return row

if __name__ == "__main__":
    row = get_random_row()
    print('./cards/' + row[1] + '.png')
