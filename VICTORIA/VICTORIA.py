import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
import openai
import spacy

# Initialize speech recognition
r = sr.Recognizer()

# Initialize natural language understanding
nlp = spacy.load("de_core_news_sm")

# Initialize OpenAI API
openai.api_key = "API-Key"

# Function to process user command


def process_command(command):
    # Check for custom commands
    if "your_custom_keyword" in command:
        # Perform your custom action here
        # Example: print a custom message
        print("Executing custom command!")

# Function to get response from ChatGPT


def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Function to convert text to speech


def convert_to_speech(text):
    tts = gTTS(text=text, lang="de")
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    temp_file_path = temp_file.name
    temp_file.close()
    tts.save(temp_file_path)
    os.system("afplay " + temp_file_path)
    os.remove(temp_file_path)


# Main loop
while True:
    try:
        # Listen for user input
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        # Recognize speech
        command = r.recognize_google(audio, language='de-DE')
        print("Recognized:", command)

        # Process user command
        process_command(command)

        # Pass user input to ChatGPT
        response = get_chatgpt_response(command)
        print("Response:", response)

        # Convert ChatGPT response to speech
        convert_to_speech(response)

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")

    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")

    except Exception as e:
        print("Sorry, an error occurred:", str(e))
