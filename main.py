# Import speech recognition library
import speech_recognition as sr

# Used to open websites in the browser
import webbrowser

# Used for text-to-speech
import edge_tts

# Used to run asynchronous functions
import asyncio

# Contains the music links
import musicLibrary

# Used to make requests to NewsAPI
import requests

# Used to play the generated voice file
import playsound

# Used to generate unique names for voice files
import uuid

# Used to delete temporary voice files
import os

# Used to connect with Groq API
from openai import OpenAI


# Create a speech recognizer
recognizer = sr.Recognizer()

# Store NewsAPI key
newsapi = "use your api"

# Connect to Groq API
client = OpenAI(
    # Groq provides an OpenAI-compatible API
    base_url="https://api.groq.com/openai/v1",

    # Your Groq API key
    api_key="use your api"
)


# Function used to make JARVIS speak
def speak(text):

    # Create a unique MP3 filename
    filename = f"voice_{uuid.uuid4()}.mp3"

    # Function to generate voice using Edge TTS
    async def voice():

        # Select Edge TTS voice
        communicate = edge_tts.Communicate(
            text,
            "en-US-GuyNeural"
        )

        # Save generated voice as an MP3 file
        await communicate.save(filename)

    # Run the voice generation function
    asyncio.run(voice())

    # Play the generated MP3 file
    playsound.playsound(filename)

    # Delete the temporary MP3 file
    try:
        os.remove(filename)
    except:
        pass


# Function to process commands using AI
def aiProcess(command):

    # Send the command to the Groq AI model
    response = client.chat.completions.create(

        # Select the AI model
        model="openai/gpt-oss-20b",

        # Give instructions to the AI and send the user's command
        messages=[
            {
                "role": "system",
                "content": "you are virtual assistant named NOVA(NOVA — Next-generation Omni-purpose Virtual Assistant) skilled in genral tasks like alexa and google cloud.give short responce please"
            },

            {
                "role": "user",
                "content": command
            }
        ]
    )

    # Return the AI's response
    return response.choices[0].message.content


# Function to process the user's command
def processCommand(c):

    # Open Google when user says "open google"
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    # Open Facebook
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    # Open YouTube
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")

    # Open LinkedIn
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")

    # Play music when command starts with "play"
    elif c.lower().startswith("play"):

        # Get the song name from the command
        song = c.lower().split(" ")[1]

        # Get the song link from musicLibrary
        link = musicLibrary.music[song]

        # Open the song link in browser
        webbrowser.open(link)

    # Get news when user asks for news
    elif "news" in c.lower():

        # Send request to NewsAPI
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        )

        # Check whether the request was successful
        if r.status_code == 200:

            # Convert the API response into JSON
            data = r.json()

            # Extract articles from the response
            articles = data.get('articles', [])

            # Speak each news headline
            for article in articles:
                speak(article['title'])

    # If command doesn't match any predefined command,
    # send it to AI
    else:

        # Send command to AI
        output = aiProcess(c)

        # Print AI response in terminal
        print("NOVA:", output)

        # Speak AI response
        speak(output)


# Main program starts here
if __name__ == "__main__":

    # Tell the user that NOVA is starting
    speak("Initializing NOVA...")

    # Keep JARVIS running continuously
    while True:

        # Create a speech recognizer
        r = sr.Recognizer()

        # Show that JARVIS is waiting for the wake word
        print("recognizing...")

        try:

            # Turn on the microphone
            with sr.Microphone() as source:

                # Display listening message
                print("Listening...")

                # Listen for the wake word
                audio = r.listen(
                    source,
                    phrase_time_limit=10
                )

            # Convert voice into text
            word = r.recognize_google(audio)

            # Print what the user said
            print("You said:", word)

            # Check if the user said "hello"
            if word.lower() == "hello":

                # Confirm that hello was detected
                print("HELLO DETECTED")

                # JARVIS responds to the wake word
                speak("hey boss")

                # Keep listening for multiple commands
                while True:

                    # Turn on the microphone
                    with sr.Microphone() as source:

                        # Show that NOVA is active
                        print("NOVA active....")

                        # Listen for the command
                        audio = r.listen(
                            source,
                            phrase_time_limit=10
                        )

                    # Convert voice command into text
                    command = r.recognize_google(audio)

                    # Print the recognized command
                    print("Command:", command)

                    # Check if the user wants to stop NOVA
                    if command.lower() == "stop":

                        # JARVIS says goodbye
                        speak("Okay boss")

                        # Completely exit the program
                        exit()

                    # Process the user's command
                    processCommand(command)

        # Handle any error without crashing the program
        except Exception as e:

            # Print the error in terminal
            print("Error; {0}".format(e))


