# app.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite Database Initialization
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return "Welcome to SCH API. See localhost:2222/users for more information."

# API Endpoints
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify({'users': users})

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name', '')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User added successfully'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the user with the given ID exists
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    if user is None:
        conn.close()
        return jsonify({'error': 'User not found'}), 404

    # Delete the user with the given ID
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': f'User with ID {user_id} deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2222)