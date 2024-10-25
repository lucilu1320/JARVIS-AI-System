# JARVIS AI System

This repository contains the code for **JARVIS**, an AI-powered virtual assistant that listens to voice commands, processes them using **Anthropic Claude API**, and responds via speech using **Eleven Labs' text-to-speech API**. It mimics the fictional assistant JARVIS from the Marvel universe, making it a personal and interactive assistant capable of answering your queries in real-time.

## Features
- **Voice Recognition**: Listens to user commands through the microphone using `speech_recognition`.
- **Natural Language Understanding**: Processes the user's query using Anthropic's Claude API.
- **Voice Response**: Converts text responses to natural-sounding speech using Eleven Labs' voice synthesis API.
- **Ambient Noise Calibration**: The system calibrates the microphone for ambient noise before listening to improve accuracy.

## Setup Instructions

### Prerequisites
- **Python 3.10**
- **Pip** for package management
- A microphone connected to your system
- **Anthropic API Key** for processing the user queries
- **Eleven Labs API Key** and **Voice ID** for the text-to-speech functionality
- **FFmpeg (Optional)**: FFmpeg can be used for more advanced audio playback and conversion needs, but it is not strictly required if platform-specific tools (`afplay`, `aplay`, `start`) are available.

### Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/lucilu1320/JARVIS-AI-System
    cd jarvis-ai-system
    ```

2. **Install Dependencies**:
    Install the required packages using pip:
    ```sh
    pip3 install -r requirements.txt
    or
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your API keys and voice ID:
    ```env
    ANTHROPIC_API_KEY=your_anthropic_api_key_here
    ELEVEN_LABS_API_KEY=your_eleven_labs_api_key_here
    ELEVEN_LABS_VOICE_ID=your_voice_id_here
    ```

### Running the Application
To start the JARVIS AI assistant:
```sh
python3 assist.py
```

JARVIS will calibrate the microphone, welcome you, and then listen for your commands. You can exit at any time by saying "exit", "quit", "goodbye", or "bye".

## Dependencies
- **Anthropic SDK**: To interact with the Anthropic Claude API.
- **SpeechRecognition**: Python library for speech recognition.
- **Eleven Labs API**: To convert text responses into natural-sounding speech.
- **Dotenv**: To manage environment variables securely.
- **FFmpeg (Optional)**: Required for advanced audio playback features, though not mandatory if using platform-specific players.

### Python Packages Used
Install these dependencies using `pip`:
```sh
pip install anthropic speechrecognition python-dotenv requests
```

## Important Notes
- Ensure that your `.env` file is correctly populated with valid API keys. Any errors related to missing API keys will be displayed upon startup.
- This project currently uses `afplay` for Mac systems, `aplay` for Linux, and `start` for Windows for audio playback. Ensure you have the appropriate player installed and accessible from your terminal.
- **FFmpeg** is optional for more advanced audio requirements.

## Project Structure
- **assist.py**: Main script for running the JARVIS AI assistant.
- **.env**: Environment configuration (not included in the repo for security purposes).
- **requirements.txt**: List of Python packages required to run the project.

## Example Commands
- "Tell me a joke."
- "What is the capital of France?"
- "Exit" to quit the assistant.

## Known Issues
- **Network Dependency**: Requires a stable internet connection to communicate with APIs.
- **Voice Model Selection**: Make sure to select an appropriate voice ID from Eleven Labs that suits your needs.

## Contributing
Feel free to open issues or submit pull requests for features, improvements, or bug fixes. Contributions are always welcome.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Anthropic** for the natural language processing capabilities.
- **Eleven Labs** for providing state-of-the-art text-to-speech voices.
- The open-source community for inspiration and guidance.
