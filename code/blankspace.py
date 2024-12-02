import speech_recognition as sr
import pyttsx3
import nltk
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


def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def listen():
  listener = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    voice = listener.listen(source)
    try:
      command = listener.recognize_google(voice)
      print(f"You said: {command}")
      return command
    except sr.UnknownValueError:
      print("Could not understand audio")
      return "None"
    except sr.RequestError as e:
      print(f"Could not request results from Google Speech Recognition service; {e}")
      return "None"
    

if __name__ == "__main__":
  while True:
    command = listen()
    if command == "None":
      continue

    # Add your specific commands and responses here
    if "hello" in command:
      speak("Hello, how can I help you?")
    elif "read" in command:
        ir=Imagereader(OS.Windows)
        text1 =ir.ext_img('Images/jpeggg.jpg' , lang='eng+rus')
        print(text1)
        text_to_speech(text1)
    elif "goodbye" in command:
      speak("Goodbye!")
      break
    else:
      speak("I didn't understand. Please try again.")





















      







    


