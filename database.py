import mysql.connector
import os
from dotenv import load_dotenv
import base64

load_dotenv()

def connect_to_database():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return conn

def create_ocr_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ocr_results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            text TEXT,
            image_data MEDIUMBLOB
        )
    ''')

def save_to_database(cursor, text, img_base64):
    cursor.execute('INSERT INTO ocr_results (text, image_data) VALUES (%s, %s)', (text, img_base64))
