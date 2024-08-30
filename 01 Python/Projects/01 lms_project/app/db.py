import mysql.connector as connection
from mysql.connector import Error

def create_connection():
    user_db = None

    try:
        user_db = connection.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "learnvista_db"
        )
        if user_db.is_connected():
            print("Successfully Connected to the database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


