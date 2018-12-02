from PIL import Image
import pytesseract

photo = "images/example_01.png"
lang = "eng"


def parsePhoto(photo="example_01.png", lang="rus"):
    try:
        f = open('text_photo.txt', 'w')
        text = pytesseract.image_to_string(Image.open(str(photo)), lang=lang)
        f.write(str(text.encode('utf-8')))
        print("\n%s" % str(text.encode('utf-8')))
    except IOError:
        print "\nError: can\'t find file or read data"


while True:
    lang = raw_input("\nWrite parsing language eng or rus: ")
    if lang.strip() == 'eng' or 'ENG' or lang.strip() == 'rus' or 'RUS':
        break

while True:
    photo = raw_input("Enter path to photo (e.g. images/example_01.png): ")
    if photo[-4:] == '.png' or photo[-4:] == '.jpg':
        break

parsePhoto(photo, lang)
