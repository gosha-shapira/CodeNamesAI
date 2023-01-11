from PIL import Image
import pytesseract
import cv2

from Extractors import CardExtractor, WordExtractor, CardExtractor1


def main():
    path = "/Users/gosha/Development/PycharmProjects/CodeNamesAI/Resources/Cards4.png"

    cards_array = CardExtractor.extract_cards_from_image(path)
    words_array = WordExtractor.extract_words_from_cards(cards_array)

    print(len(words_array))
    for word in words_array:
        print(word)


if __name__ == "__main__":
    main()
