from PIL import Image
import pytesseract
import cv2

from Extractors import CardExtractor, WordExtractor


def main():
    cards_array = CardExtractor.extract_cards_from_image(
        "/Users/gosha/Development/PycharmProjects/CodeNamesAI/Resources/Cards1.png")
    words_array = WordExtractor.extract_words_from_cards(cards_array)

    for word in words_array:
        print(word)


if __name__ == "__main__":
    main()
