import psycopg2
import csv
import os

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            phone VARCHAR(20) UNIQUE
        )
    """)
    conn.commit()

def insert_user_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("User inserted.")
    except Exception as e:
        print(e)
        conn.rollback()

def insert_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING", (row[0], row[1]))
    conn.commit()

def update_user(name, new_name=None, new_phone=None):
    if new_name:
        cur.execute("UPDATE PhoneBook SET first_name = %s WHERE first_name = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()

def query_data(filter_by=None, value=None):
    if filter_by == "name":
        cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s", (f"%{value}%",))
    elif filter_by == "phone":
        cur.execute("SELECT * FROM PhoneBook WHERE phone ILIKE %s", (f"%{value}%",))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    for row in cur.fetchall():
        print(row)

def delete_user(value):
    cur.execute("DELETE FROM PhoneBook WHERE first_name = %s OR phone = %s", (value, value))
    conn.commit()

def close():
    cur.close()
    conn.close()


# Display
menu_items = [
    "Insert user (console input)",
    "Insert users from CSV",
    "Update user",
    "Query users",
    "Delete user",
    "Exit"
]
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def print_menu():
    clear()
    print("--- PhoneBook Menu ---\n")
    for i, item in enumerate(menu_items):
        print(f"{i + 1}. {item}")
def menu_loop():
    while True:
        print_menu()
        choice = input("\nSelect an option (1-6): ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(menu_items):
                return index
        print("Invalid input. Please enter a number from 1 to 6.")
        input("Press Enter to try again...")

if __name__ == "__main__":
    create_table()

    while True:
        choice = menu_loop()

        if choice == 0:
            clear()
            insert_user_console()
            input("\nPress Enter to return to menu...")
        elif choice == 1:
            clear()
            filename = input("\nEnter CSV filename (e.g., contacts.csv): ")
            insert_from_csv(filename)
            input("\nPress Enter to return to menu...")
        elif choice == 2:
            clear()
            name = input("\n Enter name of the user to update: ")
            new_name = input("\nEnter new name (or press Enter to skip): ")
            new_phone = input("\nEnter new phone (or press Enter to skip): ")
            update_user(name, new_name if new_name else None, new_phone if new_phone else None)
            input("\nPress Enter to return to menu...")
        elif choice == 3:
            clear()
            filter_by = input("\nFilter by 'name', 'phone' or leave blank for all: ")
            value = input("\nEnter value to search (or leave blank): ")
            query_data(filter_by if filter_by else None, value if value else None)
            input("\nPress Enter to return to menu...")
        elif choice == 4:
            clear()
            value = input("\nEnter name or phone of the user to delete: ")
            delete_user(value)
            input("\nPress Enter to return to menu...")
        elif choice == 5:
            break

    close()
