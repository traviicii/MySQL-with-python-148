import mysql.connector # importing mysql conenctor library that we  pip installed
from mysql.connector import Error # importing MySQL Error package to deal with specific errors

# CRUD operations
# Create
# Retrieve
# Update
# Delete

def connect_db():
    # To establish connection to our database we need some parameters first
    db_name = "ecom"
    user = "root" # selecting which user
    password = ""
    host = "127.0.0.1" # localhost == 127.0.0.1

    # Establish our connection
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connected to MySQL database successful!")
            return conn

        
    except Error as e:
        print(f"Error: {e}")
        return None