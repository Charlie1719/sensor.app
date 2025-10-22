from flask import Flask
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/sensor')
def sensor():
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME,
            sslmode='require',
            options='-c client_encoding=UTF8'
        )
        print("Connection successful!")
        
        cursor = connection.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return f"Current Time: {result}"
    
    except Exception as e:
        return f"Failed to connect: {e}"

