from db_connection import connect_db, Error

def update_customer_phone():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            customer_id = input("what is the customer ID you'd like to update? ")
            phone = input("What is the new phone number? ")

            phone_update = (phone, customer_id)

            query = "UPDATE customer SET phone = %s WHERE id = %s;"

            cursor.execute(query, phone_update)
            conn.commit()
            print("Successfully updated customer phone number!")

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def update_customer_email():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            customer_id = input("what is the customer ID you'd like to update? ")
            email = input("what is the new email address? ")

            email_update = (email, customer_id)

            query = "UPDATE customer SET email = %s WHERE id = %s;"

            cursor.execute(query, email_update)
            conn.commit()
            print("Email successfully updated!!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def update_customer_name():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            customer_id = input("what is the customer ID you'd like to update? ")
            name = input("What is the new name? ")

            name_update = (name, customer_id)

            query = "UPDATE customer SET customer_name = %s WHERE id = %s;"

            cursor.execute(query, name_update)
            conn.commit()
            print("customer name successfully updated!! How amazing!!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
