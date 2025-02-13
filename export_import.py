import sqlite3
import csv

DB_NAME = 'travel_planner.db'

def export_csv(filename):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM trips")
    trips = c.fetchall()
    conn.close()

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Category", "Start Date", "End Date", "Cost"])
        writer.writerows(trips)

def import_csv(filename):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            c.execute("INSERT INTO trips (id, name, category, start_date, end_date, cost) VALUES (?, ?, ?, ?, ?, ?)",
                      (row[0], row[1], row[2], row[3], row[4], row[5]))
    conn.commit()
    conn.close()
