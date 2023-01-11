import cv2


def extract_cards_from_image(path: str):
    # Path to the image file
    image_path = path

    # Read the image
    image = cv2.imread(image_path)
    original = image.copy()

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use the Canny edge detector to find edges in the image
    edges = cv2.Canny(blur, 75, 200)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    card_array = []
    # Iterate through the contours
    for cnt in contours:
        # Approximate the contour as a polygon
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

        # If the contour has four vertices, it is a rectangle
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            # Extract the region of interest (ROI)
            roi = original[y:y + h, x:x + w]
            card_array.append(roi)

    return card_array
