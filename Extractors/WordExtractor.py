from PIL import Image
import pytesseract
import cv2


def process_image(image_name, lang_code):
    return pytesseract.image_to_string(Image.fromarray(image_name), lang=lang_code)


def extract_words_from_cards(cards_array):
    words_from_cards = []

    for card in cards_array:
        gray = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
        noise = cv2.medianBlur(gray, 3)
        thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY)[1]
        data_eng = process_image(thresh, "eng")
        # print(data_eng)
        words_from_cards.append(data_eng)

    return words_from_cards
