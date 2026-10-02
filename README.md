NOVA – AI Voice Assistant 🤖🎙️
NOVA is a Python-based AI-powered voice assistant that can listen to voice commands, respond using natural speech, open websites, play music, fetch news, and answer general questions using AI.
✨ Features
- 🎤 Voice command recognition
- 🤖 AI-powered responses
- 🔊 Text-to-speech using Edge TTS
- 🌐 Open websites using voice commands
- 🎵 Play music using voice commands
- 📰 Fetch and read latest news
- 👋 Wake-up command using "Hello"
- 🛑 Stop the assistant using "Stop"
- ⚡ Fast and interactive voice-based interaction
🛠️ Technologies Used
- Python
- SpeechRecognition
- Edge TTS
- Groq API
- NewsAPI
- Requests
- Playsound
- OpenAI Python SDK
📂 Project Structure
NOVA/
│
├── main.py
├── musicLibrary.py
├── requirements.txt
└── README.md

⚙️ Installation
Clone the repository:
git clone YOUR_GITHUB_REPOSITORY_URL

Go to the project folder:
cd NOVA

Install the required libraries:
pip install -r requirements.txt

🔑 API Configuration
NOVA uses Groq API for AI responses and NewsAPI for fetching news.
Add your API keys to your local environment/configuration.
Do not upload API keys or other secrets to GitHub.
▶️ Run the Project
Run:
python main.py

After starting, NOVA will initialize and wait for the wake word:
Hello

NOVA will respond:
Hey boss

You can then give multiple commands without saying Hello again.
To stop the assistant:
Stop

🎙️ Example Commands
Hello
Open Google
Open YouTube
Open Facebook
Play [song]
Give me the latest news
What is artificial intelligence?
Explain Python
Stop

🚀 Future Improvements
- Better wake-word detection
- More website commands
- Weather information
- WhatsApp and email integration
- Smart home control
- Improved conversation memory
- GUI interface
- More AI-powered features

👨‍💻 Author
Ashwin

⭐ If you like this project, consider giving the repository a star!
