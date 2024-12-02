
import pyttsx3
from PIL import Image
from pytesseract import pytesseract
import enum


class OS(enum.Enum):
    Mac = 0
    Windows = 1


class language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'


class Imagereader:
    def __init__(self, os: OS):
        if os == OS.Mac:
            print("running on mac")

        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path

    def ext_img(self, image: str, lang: str) ->str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text

def text_to_speech(text):
  """Converts text to speech.

  Args:
    text: The text to be spoken.
  """

  engine = pyttsx3.init()  # Initialize the engine
  engine.say(text)  # Set the text to be spoken
  engine.runAndWait()  # Speak the text



if __name__ == '__main__':
    ir=Imagereader(OS.Windows)
    text1 =ir.ext_img('Images/22.png' , lang='eng+rus')
    print(text1)
    text_to_speech(text1)


