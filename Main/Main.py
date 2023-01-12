from PIL import Image
import pytesseract
import cv2

from Extractors import CardExtractor, WordExtractor, ColoredCardExtractor


def main():
    path = "/Users/gosha/Development/PycharmProjects/CodeNamesAI/Resources/Board2.png"

    cards_array = CardExtractor.extract_cards_from_image(path)
    words_array = WordExtractor.extract_words_from_cards(cards_array, 'eng')
    colored_cards_array = ColoredCardExtractor.extract_colored_cards_from_image(path, 'red')
    colored_words_array = WordExtractor.extract_words_from_cards(colored_cards_array, 'eng')

    print(len(colored_words_array))
    for word in colored_words_array:
        print(word)

    print(len(words_array))
    for word in words_array:
        print(word)


if __name__ == "__main__":
    main()
