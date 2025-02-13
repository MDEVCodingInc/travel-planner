from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import csv
from database import init_db, add_trip, get_trips, get_trip_by_id, delete_trip
from export_import import export_csv, import_csv

app = Flask(__name__)

# Initialize database
init_db()

@app.route('/')
def home():
    trips = get_trips()
    return render_template('index.html', trips=trips)

@app.route('/add', methods=['POST'])
def add():
    data = request.form
    add_trip(data['name'], data['category'], data['start_date'], data['end_date'], data['cost'])
    return redirect(url_for('home'))

@app.route('/delete/<int:trip_id>')
def delete(trip_id):
    delete_trip(trip_id)
    return redirect(url_for('home'))

@app.route('/export')
def export():
    export_csv('trips.csv')
    return jsonify({'message': 'Exported to trips.csv'})

@app.route('/import', methods=['POST'])
def import_data():
    file = request.files['file']
    file.save('import.csv')
    import_csv('import.csv')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
