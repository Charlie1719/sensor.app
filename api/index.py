from flask import Flask
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
        cursor.execute('SELECT * FROM "Sensores";')
        result = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return f"Current Time: {result}"
    
    except Exception as e:
        return f"Failed to connect: {e}"

