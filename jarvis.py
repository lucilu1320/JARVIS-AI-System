from anthropic import Anthropic
import speech_recognition as sr
import os
from dotenv import load_dotenv
import subprocess
import requests
import json

class Jarvis:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        self.elevenlabs_api_key = os.getenv('ELEVEN_LABS_API_KEY')
        self.voice_id = os.getenv('ELEVEN_LABS_VOICE_ID')
        if not self.api_key:
            raise ValueError("Anthropic API key not found in .env file")
        if not self.elevenlabs_api_key:
            raise ValueError("Eleven Labs API key not found in .env file")
        if not self.voice_id:
            raise ValueError("Eleven Labs Voice ID not found in .env file")

        self.client = Anthropic(api_key=self.api_key)

        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Adjust microphone for ambient noise
        print("Calibrating microphone for ambient noise... Please wait.")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Microphone calibrated.")

    def listen(self):
        """Listen for user input through microphone"""
        with self.microphone as source:
            print("\nListening...")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing speech...")
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.WaitTimeoutError:
                print("No speech detected...")
                return None
            except sr.UnknownValueError:
                print("Could not understand audio...")
                return None
            except sr.RequestError as e:
                print(f"Speech recognition error: {e}")
                return None

    def process_query(self, text):
        """Process query using Claude API"""
        try:
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                messages=[{
                    "role": "user",
                    "content": text
                }],
                system="You are JARVIS, a highly sophisticated AI assistant. Be professional, precise, and occasionally witty. Keep responses concise yet informative. Address the user as 'sir'. Provide direct responses without any asterisks or emotion indicators."
            )

            # Extract the actual text content
            if hasattr(response.content, 'text'):
                return response.content.text
            if hasattr(response.content[0], 'text'):
                return response.content[0].text
            return str(response.content)

        except Exception as e:
            print(f"Error in processing: {e}")
            return "I apologize, sir, but I encountered an error processing your request."

    def clean_response(self, text):
        """Clean the response text"""
        # Remove asterisks, emotion indicators, and unnecessary formatting
        clean_text = str(text)
        clean_text = clean_text.replace('*', '')
        clean_text = clean_text.replace('[TextBlock(text=', '')
        clean_text = clean_text.replace('\", type=\'text\')]', '')
        clean_text = clean_text.replace('\'', '')
        return clean_text

    def speak(self, text):
        """Convert text to speech using Eleven Labs API"""
        try:
            clean_text = self.clean_response(text)
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
            headers = {
                "xi-api-key": self.elevenlabs_api_key,
                "Content-Type": "application/json"
            }
            data = {
                "text": clean_text,
                "voice_settings": {
                    "stability": 0.75,
                    "similarity_boost": 0.85
                }
            }
            response = requests.post(url, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                with open("response.mp3", "wb") as audio_file:
                    audio_file.write(response.content)
                subprocess.run(["afplay", "response.mp3"])  # Use 'afplay' for Mac, 'start' for Windows, 'aplay' for Linux
            else:
                print(f"Error in TTS response: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"Speech error: {e}")

    def run(self):
        welcome = "JARVIS online. At your service, sir. You may speak now."
        print("\nJARVIS:", welcome)
        self.speak(welcome)

        while True:
            try:
                # Get voice input
                user_input = self.listen()

                if not user_input:
                    continue

                # Check for exit commands
                if any(word in user_input.lower() for word in ['exit', 'quit', 'goodbye', 'bye']):
                    farewell = "Shutting down systems. It's been a pleasure assisting you, sir."
                    print("JARVIS:", farewell)
                    self.speak(farewell)
                    break

                # Process query and speak response
                response = self.process_query(user_input)
                clean_response = self.clean_response(response)
                print("JARVIS:", clean_response)
                self.speak(clean_response)

            except KeyboardInterrupt:
                print("\nEmergency shutdown initiated...")
                self.speak("Emergency shutdown protocol engaged. Goodbye, sir.")
                break
            except Exception as e:
                print(f"Error: {e}")
                self.speak("I apologize, sir, but I encountered an unexpected error.")

if __name__ == "__main__":
    print("Initializing JARVIS AI System...")
    try:
        assistant = Jarvis()
        assistant.run()
    except Exception as e:
        print(f"Startup Error: {e}")
        print("Please ensure your .env file contains valid API keys and your microphone is working.")

