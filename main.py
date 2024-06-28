from customer_add import add_customer
from customer_fetch import fetch_all_customers, fetch_customer

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def user_menu():
    clear()
    while True:
        action = input('''
1 - Add Customer
2 - View Customer Details
3 - Display All Customers
4 - Main Menu
''')
        
        if action == '1':
            add_customer() # Add customer stuff
        elif action == '2':
            fetch_customer() # view specific customer and stuff
        elif action == '3':
            fetch_all_customers() # display all customers stuff
        elif action == '4':
            break
        else:
            print("Are you blind?! Enter a correct numerical value for the action you wanna take.")


while True:

    action = input('''
1 - Customer Actions
2 - Book Actions
3 - Quit
''')
    
    if action == '1':
        user_menu() # customer action stuff 
    elif action == '2':
        pass # book action stuff
    elif action == '3':
        break
    else:
        print("Dude that's literally not even an option. Try again???")