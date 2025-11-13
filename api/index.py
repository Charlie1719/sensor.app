from flask import Flask,request, jsonify, render_template
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
#USER = os.getenv("user")
#PASSWORD = os.getenv("password")
#HOST = os.getenv("host")
#PORT = os.getenv("port")
#DBNAME = os.getenv("dbname")

# Fetch variables
CONNECTION_STRING = os.getenv("CONN_STRING")

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(CONNECTION_STRING)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/sensor')
def sensor():
    try:
        connection = get_connection()
        print("Connection successful!")
        
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "sensores";')
        result = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return f"Current Time: {result}"
    
    except Exception as e:
        return f"Failed to connect: {e}"

@app.route("/sensor/<int:sensor_id>", methods=["POST"])
def insert_sensor_value(sensor_id):
    value = request.args.get("value", type=float)
    if value is None:
        return jsonify({"error": "Missing 'value' query parameter"}), 400

    try:
        conn = get_connection()
        cur = conn.cursor()

        # Insert into sensors table
        cur.execute(
            "INSERT INTO sensores (sensor_id, value) VALUES (%s, %s)",
            (sensor_id, value)
        )
        conn.commit()

        return jsonify({
            "message": "Sensor value inserted successfully",
            "sensor_id": sensor_id,
            "value": value
        }), 201

    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'conn' in locals():
            conn.close()

@app.route("/hello")
def hello():
    return render_template("hello.html",user="LebronJames")

