import cv2
import sys
import os
import base64
from image_processing import process_image, display_images
from database import connect_to_database, create_ocr_table, save_to_database

if len(sys.argv) < 2:
    print("Please provide the path to the image as a command line argument.")
    sys.exit(1)

# Load image path from command line argument
image_path = sys.argv[1]

if not os.path.exists(image_path):
    print(f"The provided image path '{image_path}' does not exist. Please provide a valid image.")
    sys.exit(1)

# Image processing
img, cropped_image, text, location = process_image(image_path)

# Display intermediate images
display_images([img, cropped_image], ['Original Image', 'Cropped Image'])

# Database operations
conn = connect_to_database()
cursor = conn.cursor()

# Create OCR table if not exists
create_ocr_table(cursor)

# Convert the image to base64 format for storing in the database
_, img_encoded = cv2.imencode('.jpg', img)
img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')

# Save the text and image to the database
save_to_database(cursor, text, img_base64)

# Commit changes and close the connection
conn.commit()
conn.close()
