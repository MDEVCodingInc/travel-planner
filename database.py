import sqlite3

DB_NAME = 'travel_planner.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS trips (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    category TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    cost REAL)''')
    conn.commit()
    conn.close()

def add_trip(name, category, start_date, end_date, cost):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO trips (name, category, start_date, end_date, cost) VALUES (?, ?, ?, ?, ?)",
              (name, category, start_date, end_date, cost))
    conn.commit()
    conn.close()

def get_trips():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM trips")
    trips = c.fetchall()
    conn.close()
    return trips

def get_trip_by_id(trip_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM trips WHERE id = ?", (trip_id,))
    trip = c.fetchone()
    conn.close()
    return trip

def delete_trip(trip_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM trips WHERE id = ?", (trip_id,))
    conn.commit()
    conn.close()
