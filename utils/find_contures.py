from copy import deepcopy

import cv2
import numpy as np

import cv2
import numpy as np



def load_image_into_cv2(image):
    nparr = np.frombuffer(image.file.read(), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def find_contours(image_cv2):
    # Step 2: Preprocess the image
    gray = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  # Apply thresholding

    # Step 3: Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours



def process_image_and_return_contours(loaded_image):
    image = load_image_into_cv2(loaded_image)
    contours = find_contours(image)
    # Draw contours
    # Create a blank image with the same dimensions as the original
    blank_image = np.zeros_like(image)
    cv2.drawContours(blank_image, contours, -1, (0, 255, 0), 1)  # Draw contours in green with a thickness of 3
    return blank_image



def get_contours_positions(loaded_image):
    image = load_image_into_cv2(loaded_image)
    contours = find_contours(image)
    # Get the position of the contours
    positions = [cv2.boundingRect(contour) for contour in contours]
    return positions


def get_display_contours_positions(loaded_image):
    image = load_image_into_cv2(deepcopy(loaded_image))
    positions = get_contours_positions(loaded_image)
    # Draw contours on the image using OpenCV
    for x, y, w, h in positions:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle around the contours
    return image