import psycopg2
import os
import csv

try:
    conn = psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
except Exception as e:
    print(f"Ошибка подключения к БД: {e}")
    exit(1)

menu_items = [
    "Insert user (console input)",
    "Insert users from CSV",
    "Upsert user (no procedure)",
    "Insert many users (no procedure)",
    "Search (pattern)",
    "Paginate results",
    "Delete user (no procedure)",
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
        choice = input("\nSelect an option (1-8): ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(menu_items):
                return index
        print("Invalid input. Please enter a number from 1 to 8.")
        input("Press Enter to try again...")

def insert_user_console():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    try:
        cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("User inserted.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def insert_from_csv(filename):
    if not os.path.isfile(filename):
        print("File not found.")
        return
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    cur.execute(
                        "INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                        (row[0], row[1])
                    )
        conn.commit()
        print("CSV data inserted.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def upsert_user():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    try:
        cur.execute("""
            INSERT INTO PhoneBook (first_name, phone)
            VALUES (%s, %s)
            ON CONFLICT (phone)
            DO UPDATE SET first_name = EXCLUDED.first_name
        """, (name, phone))
        conn.commit()
        print("User upserted.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def insert_many_users():
    names = input("Enter names (comma-separated): ").split(",")
    phones = input("Enter phones (comma-separated): ").split(",")
    names = [n.strip() for n in names]
    phones = [p.strip() for p in phones]

    if len(names) != len(phones):
        print("Name and phone counts must match!")
        return

    invalid = []
    try:
        for name, phone in zip(names, phones):
            try:
                cur.execute("""
                    INSERT INTO PhoneBook (first_name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (phone) DO NOTHING
                """, (name, phone))
            except Exception:
                invalid.append((name, phone))
        conn.commit()
        if invalid:
            print("Invalid entries (possibly duplicates or errors):")
            for i in invalid:
                print(" -", i)
        else:
            print("All users inserted.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def search_pattern():
    pattern = input("Enter pattern to search: ").strip()
    try:
        like_pattern = f"%{pattern}%"
        cur.execute("""
            SELECT * FROM PhoneBook
            WHERE first_name ILIKE %s OR phone ILIKE %s
        """, (like_pattern, like_pattern))
        results = cur.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No matches found.")
    except Exception as e:
        print(f"Error: {e}")

def paginate_results():
    try:
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        cur.execute("""
            SELECT * FROM PhoneBook
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (limit, offset))
        results = cur.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No results on this page.")
    except Exception as e:
        print(f"Error: {e}")

def delete_user():
    val = input("Enter name or phone to delete: ").strip()
    try:
        cur.execute("""
            DELETE FROM PhoneBook
            WHERE first_name = %s OR phone = %s
        """, (val, val))
        conn.commit()
        print("User(s) deleted.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def close():
    cur.close()
    conn.close()

if __name__ == "__main__":
    try:
        while True:
            choice = menu_loop()
            clear()
            if choice == 0:
                insert_user_console()
            elif choice == 1:
                filename = input("Enter CSV filename: ").strip()
                insert_from_csv(filename)
            elif choice == 2:
                upsert_user()
            elif choice == 3:
                insert_many_users()
            elif choice == 4:
                search_pattern()
            elif choice == 5:
                paginate_results()
            elif choice == 6:
                delete_user()
            elif choice == 7:
                break
            input("\nPress Enter to return to menu...")
    finally:
        close()