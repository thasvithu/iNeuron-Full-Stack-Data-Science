import mysql.connector as connection
from mysql.connector import Error

def create_connection():
    user_db = None

    try:
        user_db = connection.connect(
            host = "us-cluster-east-01.k8s.cleardb.net",
            user = "b693725dbe44f6",
            password = "ac1c1439",
            database = "heroku_a5aac21fbd25659"
        )
        if user_db.is_connected():
            return  user_db
    except Error as e:
        print(f"The error '{e}' occurred")
    return None
