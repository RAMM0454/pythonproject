import speech_recognition as sr
import pyttsx3
import nltk

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
    elif "goodbye" in command:
      speak("Goodbye!")
      break
    else:
      speak("I didn't understand. Please try again.")