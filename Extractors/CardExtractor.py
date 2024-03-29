import cv2


def extract_cards_from_image(path: str):
    # Extract cards from given big image, and returns array of the cards one-by-one
    img_path = path
    image = cv2.imread(img_path)
    original = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    image_number = 0
    card_array = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 3)
        ROI = original[y:y + h, x:x + w]
        cv2.imwrite("/Users/gosha/Development/PycharmProjects/CodeNamesAI/Extractors/extracted/ROI_{}.png".format(image_number), ROI)
        card_array.append(ROI)
        image_number += 1

    return card_array
