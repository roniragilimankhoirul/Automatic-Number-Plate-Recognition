import mysql.connector
from io import BytesIO
import base64
from matplotlib import pyplot as plt
import cv2
import numpy as np
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return conn

def fetch_and_display_image(cursor, index=None):
    # Fetch all rows from the database
    cursor.execute('SELECT id, text, image_data FROM ocr_results')
    results = cursor.fetchall()

    if not results:
        print("No results found in the database.")
        return

    if index is not None:
        if 0 <= index < len(results):
            result = results[index]
            display_image(result)
        else:
            print(f"Invalid index: {index}. Index should be between 0 and {len(results) - 1}.")
    else:
        # Set up subplots
        num_results = len(results)
        num_cols = 2  # You can adjust the number of columns as needed
        num_rows = (num_results + num_cols - 1) // num_cols
        fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

        for idx, result in enumerate(results):
            if num_rows == 1:
                col = idx % num_cols
                display_image(result, ax=axes[col])
            else:
                row = idx // num_cols
                col = idx % num_cols
                display_image(result, ax=axes[row, col])

        # Adjust layout for better visualization
        plt.tight_layout()
        plt.show()

def display_image(result, ax=None):
    id, text, img_base64 = result

    # Convert base64-encoded image data to bytes
    img_bytes = base64.b64decode(img_base64)

    # Convert bytes to image
    img_np = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    # Plot the image in the specified subplot or a new plot
    if ax is not None:
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(f'ID: {id}, Text: {text}')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(f'ID: {id}, Text: {text}')
        plt.show()

if __name__ == "__main__":
    # Connect to MySQL database
    conn = connect_to_database()

    cursor = conn.cursor()

    if len(sys.argv) == 1:
        # No command line arguments provided, display all images
        fetch_and_display_image(cursor)
    elif len(sys.argv) == 2:
        # One command line argument provided, assume it's an index
        try:
            index = int(sys.argv[1])
            fetch_and_display_image(cursor, index)
        except ValueError:
            print("Invalid argument. Please provide a valid index or no arguments to display all images.")
    else:
        print("Invalid number of command line arguments. Please provide a valid index or no arguments to display all images.")

    # Close the connection
    conn.close()
