#Author Pullisani Satvika
import sqlite3

conn = sqlite3.connect('railway_system.db')
c = conn.cursor()

def create_DB_if_Not_available():
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (username TEXT, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                (employee_id TEXT, password TEXT, designation TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS trains
                (train_number TEXT, train_name TEXT, departure_date TEXT, starting_destination TEXT, 
                ending_destination TEXT)''')
    conn.commit()

def add_train(train_number, train_name, departure_date, starting_destination, ending_destination):
    c.execute("INSERT INTO trains (train_number, train_name, departure_date, starting_destination, ending_destination) VALUES (?, ?, ?, ?, ?)",
              (train_number, train_name, departure_date, starting_destination, ending_destination))
    conn.commit()
    create_seat_table(train_number)

def delete_train(train_number, departure_date):
    train_query = c.execute("SELECT * FROM trains WHERE train_number = ?", (train_number,))
    train_data = train_query.fetchone()
    if train_data:
        c.execute("DELETE FROM trains WHERE train_number = ? AND departure_date=?", (train_number, departure_date))
        conn.commit()
        print(f"Train with Train Number {train_number} has been deleted.")
    else:
        print(f"No such Train with Number {train_number} is available")

def create_seat_table(train_number):
    c.execute(f'''
                CREATE TABLE IF NOT EXISTS seats_{train_number} (
                    seat_number INTEGER PRIMARY KEY,
                    seat_type TEXT,
                    booked INTEGER,
                    passenger_name TEXT,
                    passenger_age INTEGER,
                    passenger_gender TEXT
                )
            ''')
    for i in range(1, 51):
        val = categorize_seat(i)
        c.execute(f'''INSERT INTO seats_{train_number}(seat_number, seat_type, booked, passenger_name, passenger_age, passenger_gender) VALUES (?,?,?,?,?,?);''', (
            i, val, 0, "", "", ""))
        conn.commit()

def categorize_seat(seat_number):
    if (seat_number % 10) in [0, 4, 5, 9]:
        return "Window"
    elif (seat_number % 10) in [2, 3, 6, 7]:
        return "Aisle"
    else:
        return "Middle"

def allocate_next_available_seat(train_number, seat_type):
    seat_query = c.execute(f"SELECT seat_number FROM seats_{train_number} WHERE booked=0 and seat_type=? ORDER BY seat_number asc", (seat_type,))
    result = seat_query.fetchall()
    if result:
        return result[0]

def book_ticket(train_number, passenger_name, passenger_age, passenger_gender, seat_type):
    train_query = c.execute("SELECT * FROM trains WHERE train_number = ?", (train_number,))
    train_data = train_query.fetchone()
    if train_data:
        seat_number = allocate_next_available_seat(train_number, seat_type)
        if seat_number:
            c.execute(f"UPDATE seats_{train_number} SET booked=1, seat_type=?, passenger_name=?, passenger_age=?, passenger_gender=? WHERE seat_number=?", (
                seat_type, passenger_name, passenger_age, passenger_gender, seat_number[0]))
            conn.commit()
            print(f"Successfully booked seat {seat_number[0]} ({seat_type}) for {passenger_name}.")
        else:
            print("No available seats for booking in this train.")
    else:
        print(f"No such Train with Number {train_number} is available")

def cancel_tickets(train_number, seat_number):
    train_query = c.execute("SELECT * FROM trains WHERE train_number = ?", (train_number,))
    train_data = train_query.fetchone()
    if train_data:
        c.execute(f'''UPDATE seats_{train_number} SET booked=0, passenger_name='', passenger_age='', passenger_gender='' WHERE seat_number=?''', (seat_number,))
        conn.commit()
        print(f"Successfully booked seat {seat_number} from {train_number} .")
    else:
        print(f"No such Train with Number {train_number} is available")

def search_train_by_train_number(train_number):
    train_query = c.execute("SELECT * FROM trains WHERE train_number = ?", (train_number,))
    train_data = train_query.fetchone()
    return train_data

def search_trains_by_destinations(starting_destination, ending_destination):
    train_query = c.execute("SELECT * FROM trains WHERE starting_destination = ? AND ending_destination = ?", (starting_destination, ending_destination))
    train_data = train_query.fetchall()
    return train_data

def view_seats(train_number):
    train_query = c.execute("SELECT * FROM trains WHERE train_number = ?", (train_number,))
    train_data = train_query.fetchone()
    if train_data:
        seat_query = c.execute(f'''SELECT 'Number : ' || seat_number, '\n Type : ' || seat_type ,'\n Name : ' || passenger_name , '\n Age : ' || passenger_age ,'\n Gender : ' || passenger_gender as Details, booked FROM seats_{train_number} ORDER BY seat_number asc''')
        result = seat_query.fetchall()
        if result:
            print(result)
        else:
            print(f"No such Train with Number {train_number} is available")

# Close the database connection
conn.close()
