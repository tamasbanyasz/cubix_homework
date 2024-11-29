from Feelings_package import DatabaseUnity as du
from Feelings_package import Feelings
from Feelings_package import database_backup
from Feelings_package import database_restore
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from time import time

create_feelings_table = """
CREATE TABLE IF NOT EXISTS feelings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feeling TEXT NOT NULL,
    first_moment REAL,
    second_moment REAL,
    third_moment REAL
);
"""

create_another_table = """
CREATE TABLE IF NOT EXISTS another (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feelingid INTEGER,
    moments TEXT,
    feeling_value REAL,
    FOREIGN KEY(feelingid) REFERENCES feelings(id)
);
"""

insert_to_feelings_table = """
INSERT INTO feelings(feeling, first_moment, second_moment, third_moment) VALUES (?, ?, ?, ?);
"""

insert_to_another_table = """
INSERT INTO another(moments, feelingid, feeling_value) VALUES (?, ?, ?);
"""

database_path = r"./Feelings_package/feelingdb.db"
backup_dir = r"./Feelings_package/db_backup/dir"  

# Többszálú adatfeldolgozási funkciók
def process_feelings_data(obj):
    """
    Feldolgozza a feelings táblához szükséges adatokat.
    """
    with du.create_connection(database_path) as conn:
        obj.append_datas_to_starter_dataframe()

        # Indexek helyes beállítása
        obj.starter_df.index += len(conn.cursor().execute('SELECT * FROM feelings;').fetchall()) + 1

        feelings_data = obj.starter_df.iloc[:, :4].to_records(index=False).tolist()

        cursor = conn.cursor()
        cursor.executemany(insert_to_feelings_table, feelings_data)
        print("Data to 'feelings' table has been sent.")
        
        print("\nSelect all data from 'feelins' table:")
        du.select_all_data(conn, 'SELECT * FROM feelings;')

def process_another_data(obj):
    """
    Feldolgozza az another táblához szükséges adatokat.
    """
    with du.create_connection(database_path) as conn:
        another_data = pd.concat(obj.feelings_one_by_one(), axis=0).T.drop_duplicates().T.drop_duplicates().reset_index(drop=True)
                
        if another_data.empty:
            print("No data to insert into 'another' table.")
            return  

        cursor = conn.cursor()
        cursor.executemany(insert_to_another_table, another_data.itertuples(index=False))
        print("Data to 'another' table has been sent.")
        
        
        print("\nSelect all data from 'another' table:")
        du.select_all_data(conn, 'SELECT * FROM another;')


def main():
    start = time()
    obj = Feelings()

    # Adatbázis inicializálás
    with du.create_connection(database_path) as conn:
        cursor = conn.cursor()
        du.create_table(cursor, create_feelings_table)
        du.create_table(cursor, create_another_table)
    
    # Többszálú feldolgozás
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(process_feelings_data, obj)
        future1.result()  # Megvárjuk az első szál befejeződését

        future2 = executor.submit(process_another_data, obj)
        future2.result()  # Megvárjuk a második szál befejeződését

    # Inner join tesztelése
    with du.create_connection(database_path) as conn:
        print("\nInner join query:")
        du.inner_join_query(conn)

    end = time()
    print(f"\nExecution time: {end - start:.2f} seconds")
    
    database_backup.backup_database(database_path, backup_dir)
    
    input_datetime = '2024-11-29 16:48:56'
    database_restore.restore_database(backup_dir, input_datetime, database_path)
    
    print("Restored db: ")
    with du.create_connection(database_path) as conn:
        print("\nInner join query:")
        du.inner_join_query(conn)


if __name__ == "__main__":
    main()
    print("Make a change whit this")
   


