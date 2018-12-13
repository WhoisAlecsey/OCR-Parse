from PIL import Image
import pytesseract
import substring

formatOfImage = ['.png', '.jpg']
languages = ['eng', 'rus']

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
    if lang.strip() in languages:
        break
    else:
        print "Unknown language."

while True:
    path = raw_input("Enter path to photo (e.g. images/example_01.png): ")
    typeOfImage = substring.substringByChar(path, startChar=".")
    if typeOfImage in formatOfImage:
        break
    else:
        print "Unknown format."

parsePhoto(path, lang)
