from db_connection import connect_db, Error

def add_customer():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is your name? ").title()
            email = input("What is your email? ")
            phone = input("Phone: ")

            new_customer = (name, email, phone)

            query = "INSERT INTO customer (customer_name, email, phone) VALUES (%s, %s, %s)"

            cursor.execute(query, new_customer)
            conn.commit() # Fully commits the changes we are trying to make (adding data to the customer table)
            print(f"New cutomser {name} added successfully!")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close() # ALWAYS

