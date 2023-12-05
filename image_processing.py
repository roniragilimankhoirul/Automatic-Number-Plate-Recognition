import cv2
import numpy as np
import easyocr
import imutils
from matplotlib import pyplot as plt

def process_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Display the original image using matplotlib
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.show()

    # Noise reduction using bilateral filter
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)

    # Edge detection using Canny
    edged = cv2.Canny(bfilter, 30, 200)

    # Display the edged image using matplotlib
    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    plt.title("Edged Image")
    plt.show()

    # Find contours and sort by area, keeping the top 10
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    # Find the location of the document
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    # Display the location
    print("Document Location:", location)

    # Create a mask and extract the region of interest
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    # Display the masked image using matplotlib
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    plt.title("Masked Image")
    plt.show()

    # Crop the image based on the location
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]

    # Display the cropped image using matplotlib
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.title("Cropped Image")
    plt.show()

    # Perform OCR on the cropped image
    reader = easyocr.Reader(['id', 'en'])
    result = reader.readtext(cropped_image)
    text = result[0][-2]

    # Draw bounding box and text on the original image
    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(img, text=text, org=(location[0][0][0], location[1][0][1]+60), fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    res = cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0, 255, 0), 3)

    # Display the final result
    plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    plt.title("Final Result")
    plt.show()

    return img, cropped_image, text, location

# Example usage:
# img, cropped_image, text, location = process_image('path/to/your/image.jpg')
# from matplotlib import pyplot as plt

def display_images(images, titles):
    for i, (image, title) in enumerate(zip(images, titles), 1):
        plt.subplot(1, len(images), i)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis("off")
    plt.show()
