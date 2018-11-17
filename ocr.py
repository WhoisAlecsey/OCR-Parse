from PIL import Image
import pytesseract


def parsePhoto(photo = "example_01.png", lang = "eng"):
    f = open('text_photo.txt', 'w')
    text = pytesseract.image_to_string(Image.open(str(photo)), lang=lang)
    f.write(str(text.encode('utf-8')))
    print("\n%s" % str(text.encode('utf-8')))


print("Enter photo name with type and lang:\n\tFor Example:\n\texample_01.png\n\teng")
photo = "images/%s" % raw_input()
lang = "%s" % raw_input()

parsePhoto(photo, lang)