import sqlite3
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Database:
    def __init__(self):
        pass

    def Create_table(self):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            try:
                cursor = con.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS RecordSystem(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               Item TEXT,
                               Quantity INTEGER,
                               Amount INTEGER,
                               Date TEXT,
                               time TEXT
                               )""")
            except Exception as e:
                print(e)
    
    def insert_data(self,data):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            try:
                cursor = con.cursor()
                values = ",".join(['?'] * len(data)) 
                query = f"""INSERT INTO RecordSystem (Item,Quantity,Amount,Date,Time)
                VALUES ({values})
                """
                cursor.execute(query,data)
                con.commit()
            except Exception as e:
                print(e)

    def view_date_and_time(self):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()  
            try:
                cursor.execute("SELECT Date,time FROM RecordSystem")
                return cursor.fetchall()
            except Exception as e:
                print(e)
    
    def view_data(self):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM RecordSystem")
            return cursor.fetchall()

    def get_data_by_date(self,start_date,end_date):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            try:
                query = """SELECT * FROM RecordSystem
                WHERE Date BETWEEN ? AND ?
                """
                cursor.execute(query,(start_date,end_date))
                return cursor.fetchall()
            except Exception as e:
                print(e)

    def get_expenses_by_date(self,start_date,end_date):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            try:
                query = """
                SELECT SUM(Amount) FROM RecordSystem
                WHERE Date BETWEEN ? AND ?
                """
                cursor.execute(query,(start_date,end_date))
                return cursor.fetchall()
            except Exception as e:
                print(e)

    def delete_data(self,Id):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            try:
                cursor.execute("DELETE FROM RecordSystem WHERE id = ?",Id)
                con.commit()
            except Exception as e:
                print(e)

    def update(self,item,quantity,amount,Id):
        db_path = resource_path("Database_folder/Date.db")

        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            try:
                cursor.execute("""UPDATE RecordSystem 
                               SET Item = ?,
                               Quantity = ?,
                               Amount = ?
                               WHERE id = ?
                               """,(item,quantity,amount,Id))
            except Exception as e:
                print(e)


