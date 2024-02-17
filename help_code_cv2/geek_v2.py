# Import required packages
import cv2
import pytesseract

# Read image from which text needs to be extracted
img = cv2.imread("diff.png")

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()

# Looping through the identified contours and drawing rectangles
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with rectangles
cv2.imshow('Detected Text Areas', im2)
cv2.waitKey(0)  # Waits for a key press to close the window
cv2.destroyAllWindows()  # Closes the window and releases resources

# Note: The OCR part and writing to file are omitted in this snippet for clarity.
