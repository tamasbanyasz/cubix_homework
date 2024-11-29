import sqlite3
from sqlite3 import Error
import os


class DatabaseUnity:
    def __init__(self):
        pass
    
    @classmethod
    def create_connection(cls, db_file):
        try:
            if not os.path.exists(os.path.dirname(db_file)):
                os.makedirs(os.path.dirname(db_file))
            conn = sqlite3.connect(db_file)
            print(f"Kapcsolat létrejött az adatbázishoz: {db_file}")
            print("Adatbázis útvonal:", os.path.abspath(db_file))
            return conn
        except sqlite3.Error as e:
            print(f"Hiba történt az adatbázis-kapcsolat létrehozásakor: {e}")
            return None
        
    @classmethod
    def create_table(cls, conn, create_sql_table):
    
        try:    
            conn.execute(create_sql_table)
    
        except Error as e:
            print(e) 
    
    @classmethod
    def insert_to_table(cls, conn, insert, value):
    
        cur = conn.cursor()
        cur.execute(insert, value)
        conn.commit()
    
        return cur.lastrowid
    
    @classmethod
    def select_all_data(cls, conn, select_all_data):
    
        cur = conn.cursor()
        cur.execute(select_all_data)
    
        rows = cur. fetchall()
    
        for row in rows:
            print(row)

    @classmethod   
    def inner_join_query(cls, conn):
    
        cur = conn.cursor()
        cur.execute('''
                
                    SELECT feelings.id, 
                            another.feelingid, 
                            feelings.feeling, 
                            feelings.first_moment, 
                            another.moments, 
                            another.feeling_value
                         
                    FROM feelings 
                    INNER JOIN another 
                    ON feelings.id = another.feelingid;
                
                    ''')
        
        rows = cur.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    DatabaseUnity()
    
    