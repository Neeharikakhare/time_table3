from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
# Enable CORS so your frontend can communicate with this API
CORS(app) 

# --- Database Setup ---
def get_db_connection():
    conn = sqlite3.connect('timetable.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # Create tables if they don't exist
    conn.execute('''CREATE TABLE IF NOT EXISTS faculties 
                    (id TEXT PRIMARY KEY, name TEXT, desig TEXT, phone TEXT, email TEXT, in_time TEXT, out_time TEXT)''')
    
    conn.execute('''CREATE TABLE IF NOT EXISTS subjects 
                    (id TEXT PRIMARY KEY, name TEXT, branch TEXT, sem TEXT, code TEXT, type TEXT, credits INTEGER)''')
    
    conn.execute('''CREATE TABLE IF NOT EXISTS mappings 
                    (id TEXT PRIMARY KEY, facId TEXT, subId TEXT, lectures INTEGER, batch TEXT)''')
    
    conn.execute('''CREATE TABLE IF NOT EXISTS timetable 
                    (cell_id TEXT PRIMARY KEY, map_id TEXT)''')
    
    conn.commit()
    conn.close()

init_db()

# --- API Endpoints ---

@app.route('/api/faculties', methods=['GET', 'POST'])
def manage_faculties():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.json
        conn.execute('INSERT INTO faculties (id, name, desig, phone, email, in_time, out_time) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (data['id'], data['name'], data['desig'], data['phone'], data['email'], data['in'], data['out']))
        conn.commit()
        conn.close()
        return jsonify({"status": "Faculty added"}), 201
    
    faculties = conn.execute('SELECT * FROM faculties').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in faculties])

@app.route('/api/subjects', methods=['GET', 'POST'])
def manage_subjects():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.json
        conn.execute('INSERT INTO subjects (id, name, branch, sem, code, type, credits) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (data['id'], data['name'], data['branch'], data['sem'], data['code'], data['type'], data['credits']))
        conn.commit()
        conn.close()
        return jsonify({"status": "Subject added"}), 201
    
    subjects = conn.execute('SELECT * FROM subjects').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in subjects])

@app.route('/api/mappings', methods=['GET', 'POST'])
def manage_mappings():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.json
        conn.execute('INSERT INTO mappings (id, facId, subId, lectures, batch) VALUES (?, ?, ?, ?, ?)',
                     (data['id'], data['facId'], data['subId'], data['lectures'], data['batch']))
        conn.commit()
        conn.close()
        return jsonify({"status": "Mapping added"}), 201
    
    mappings = conn.execute('SELECT * FROM mappings').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in mappings])

@app.route('/api/timetable', methods=['GET', 'POST', 'DELETE'])
def manage_timetable():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.json
        # Insert or replace the cell assignment
        conn.execute('REPLACE INTO timetable (cell_id, map_id) VALUES (?, ?)',
                     (data['cell_id'], data['map_id']))
        conn.commit()
        conn.close()
        return jsonify({"status": "Cell updated"}), 200
        
    elif request.method == 'DELETE':
        data = request.json
        conn.execute('DELETE FROM timetable WHERE cell_id = ?', (data['cell_id'],))
        conn.commit()
        conn.close()
        return jsonify({"status": "Cell cleared"}), 200

    timetable = conn.execute('SELECT * FROM timetable').fetchall()
    conn.close()
    # Convert list of rows to a dictionary format: {"Monday_08:30 - 09:20": "map_id"}
    tt_dict = {row['cell_id']: row['map_id'] for row in timetable}
    return jsonify(tt_dict)

if __name__ == '__main__':
    app.run(debug=True, port=5000)