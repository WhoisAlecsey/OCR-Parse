from PIL import Image
import pytesseract

photo = "images/example_01.png"
lang = "eng"

def parsePhoto(photo="example_01.png", lang="rus"):
    f = open('text_photo.txt', 'w')
    text = pytesseract.image_to_string(Image.open(str(photo)), lang=lang)
    f.write(str(text.encode('utf-8')))
    print("\n%s" % str(text.encode('utf-8')))

print("Write parsing language:\neng or rus")
lang = raw_input()
print("Enter path to photo:\n\tFor Example:\n\timages/example_01.png")

photo = "%s" % raw_input()

parsePhoto(photo, lang)