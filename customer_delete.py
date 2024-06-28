from db_connection import connect_db, Error

def delete_customer(customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "DELETE FROM orders WHERE customer_id = %s;"
            cursor.execute(query, (customer_id,))
            conn.commit()

            # customer_id = input("what customer id would you like to delete? ")

            query = "DELETE FROM customer WHERE id = %s;"

            cursor.execute(query, (customer_id,))
            conn.commit() # NEVER FORGET
            print("Customer successfully deleted!! Wow!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close() # NEVERRRRRR FORGET!! O_O

# def delete_customer_orders(customer_id):
#     conn = connect_db()
#     if conn is not None:
#         try:
#             cursor = conn.cursor()

#             query = "DELETE FROM orders WHERE customer_id = %s;"
#             cursor.execute(query, (customer_id,))
#             conn.commit()

delete_customer(10)