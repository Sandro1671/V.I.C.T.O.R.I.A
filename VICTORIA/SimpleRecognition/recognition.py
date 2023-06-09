import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Listen for audio input
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

# Recognize speech
try:
    command = r.recognize_google(audio, language='de-DE')
    print("Recognized:", command)
except sr.UnknownValueError:
    print("Sorry, I didn't catch that. Please try again.")
except sr.RequestError:
    print("Sorry, there was an issue with the speech recognition service.")
