import cv2


def extract_colored_cards_from_image(path: str, color: str):
    # Extract cards from given big image, and returns array of the cards one-by-one
    img_path = path
    image = cv2.imread(img_path)
    original = image.copy()
    color_lower = color.lower()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if color_lower == 'blue':
        # Define the range of blue color in HSV ----> todo: need to handle if background is in the same color
        blue_lower = (50, 50, 110)
        blue_upper = (130, 255, 255)
        mask = cv2.inRange(hsv, blue_lower, blue_upper)

    if color_lower == 'red':
        # Define the range of red color in HSV ----> todo: need to handle if background is in the same color
        red_lower = (0, 50, 50)
        red_upper = (10, 255, 255)
        mask = cv2.inRange(hsv, red_lower, red_upper)

    if color_lower == 'black':
        # Define the range of black color in HSV ----> todo: need to precise
        black_lower = (23, 0, 0)
        black_upper = (80, 105, 107)
        mask = cv2.inRange(hsv, black_lower, black_upper)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    image_number = 0
    card_array = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 3)
        ROI = original[y:y + h, x:x + w]
        # cv2.imwrite("/Users/gosha/Development/PycharmProjects/CodeNamesAI/Extractors/extracted/ROI_{}.png".format(image_number), ROI)
        card_array.append(ROI)
        image_number += 1

    return card_array
