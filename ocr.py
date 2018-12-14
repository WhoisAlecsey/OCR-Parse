from PIL import Image
import pytesseract
import substring

formatOfImage = ['.png', '.jpg', '.jpeg']
languages = ['eng', 'rus']


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
        print "Unknown language: " + lang.strip()

while True:
    path = raw_input("Enter path to photo (e.g. images/example_01.png): ")
    typeOfImage = substring.substringByChar(path[path.rfind("."):], startChar=".")

    if typeOfImage in formatOfImage:
        photo = path
        break
    else:
        print "Unknown format: " + typeOfImage

parsePhoto(photo, lang)
