from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connect to RDS MySQL database
db = mysql.connector.connect(
    host="database-1.ca9a0e62indh.us-east-1.rds.amazonaws.com",
    user="admin",
    password="mahammadtaj",
    database="haircut_db"
)
cursor = db.cursor()

# API to book an appointment
@app.route('/book', methods=['POST'])
def book_appointment():
    data = request.json
    name = data['name']
    phone = data['phone']
    cursor.execute("INSERT INTO appointments (name, phone) VALUES (%s, %s)", (name, phone))
    db.commit()
    return jsonify({"message": "Appointment booked successfully!"})

# API to view all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    cursor.execute("SELECT * FROM appointments")
    return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
