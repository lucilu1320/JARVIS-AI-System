# JARVIS-AI-System
An AI coded in Python.

# Description
This repository contains the code for JARVIS, an AI-powered virtual assistant that listens to voice commands, processes them using Anthropic Claude API, and responds via speech using Eleven Labs' text-to-speech API. It mimics the fictional assistant JARVIS from the Marvel universe, making it a personal and interactive assistant capable of answering your queries in real-time.

# Features
1. Voice Recognition: Listens to user commands through the microphone using speech_recognition.
2. Natural Language Understanding: Processes the user's query using Anthropic's Claude API.
3. Voice Response: Converts text responses to natural-sounding speech using Eleven Labs' voice synthesis API.
4. Ambient Noise Calibration: The system calibrates the microphone for ambient noise before listening to improve accuracy.

# Setup Instructions
<h3>Prerequisites</h3>
<li></li>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JARVIS AI System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #444;
        }
        pre {
            background: #f8f8f8;
            padding: 10px;
            overflow-x: auto;
            border-radius: 5px;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }
        ul {
            margin: 20px 0;
            padding-left: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>JARVIS AI System</h1>
        <p>This repository contains the code for <strong>JARVIS</strong>, an AI-powered virtual assistant that listens to voice commands, processes them using <strong>Anthropic Claude API</strong>, and responds via speech using <strong>Eleven Labs' text-to-speech API</strong>. It mimics the fictional assistant JARVIS from the Marvel universe, making it a personal and interactive assistant capable of answering your queries in real-time.</p>
        
        <h2>Features</h2>
        <ul>
            <li><strong>Voice Recognition</strong>: Listens to user commands through the microphone using <code>speech_recognition</code>.</li>
            <li><strong>Natural Language Understanding</strong>: Processes the user's query using Anthropic's Claude API.</li>
            <li><strong>Voice Response</strong>: Converts text responses to natural-sounding speech using Eleven Labs' voice synthesis API.</li>
            <li><strong>Ambient Noise Calibration</strong>: The system calibrates the microphone for ambient noise before listening to improve accuracy.</li>
        </ul>

        <h2>Setup Instructions</h2>

        <h3>Prerequisites</h3>
        <ul>
            <li><strong>Python 3.7+</strong></li>
            <li><strong>Pip</strong> for package management</li>
            <li>A microphone connected to your system</li>
            <li><code>ffmpeg</code> installed (required for playing audio on different platforms)</li>
            <li><strong>Anthropic API Key</strong> for processing the user queries</li>
            <li><strong>Eleven Labs API Key</strong> and <strong>Voice ID</strong> for the text-to-speech functionality</li>
        </ul>

        <h3>Installation</h3>
        <ol>
            <li><strong>Clone the repository</strong>:
                <pre><code>git clone https://github.com/yourusername/jarvis-ai-system.git
cd jarvis-ai-system</code></pre>
            </li>
            <li><strong>Install Dependencies</strong>: Install the required packages using pip:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Configure Environment Variables</strong>: Create a <code>.env</code> file in the root directory and add your API keys and voice ID:
                <pre><code>ANTHROPIC_API_KEY=your_anthropic_api_key_here
ELEVEN_LABS_API_KEY=your_eleven_labs_api_key_here
ELEVEN_LABS_VOICE_ID=your_voice_id_here</code></pre>
            </li>
        </ol>

        <h3>Running the Application</h3>
        <p>To start the JARVIS AI assistant:</p>
        <pre><code>python3 assist.py</code></pre>
        <p>JARVIS will calibrate the microphone, welcome you, and then listen for your commands. You can exit at any time by saying "exit", "quit", "goodbye", or "bye".</p>

        <h2>Dependencies</h2>
        <ul>
            <li><strong>Anthropic SDK</strong>: To interact with the Anthropic Claude API.</li>
            <li><strong>SpeechRecognition</strong>: Python library for speech recognition.</li>
            <li><strong>Eleven Labs API</strong>: To convert text responses into natural-sounding speech.</li>
            <li><strong>Dotenv</strong>: To manage environment variables securely.</li>
            <li><strong>FFmpeg</strong>: Required for audio playback on different platforms.</li>
        </ul>

        <h3>Python Packages Used</h3>
        <pre><code>pip install anthropic speechrecognition python-dotenv requests</code></pre>

        <h2>Important Notes</h2>
        <ul>
            <li>Ensure that your <code>.env</code> file is correctly populated with valid API keys. Any errors related to missing API keys will be displayed upon startup.</li>
            <li>This project currently uses <code>afplay</code> for Mac systems, <code>aplay</code> for Linux, and <code>start</code> for Windows for audio playback. Ensure you have the appropriate player installed and accessible from your terminal.</li>
        </ul>

        <h2>Project Structure</h2>
        <ul>
            <li><strong>assist.py</strong>: Main script for running the JARVIS AI assistant.</li>
            <li><strong>.env</strong>: Environment configuration (not included in the repo for security purposes).</li>
            <li><strong>requirements.txt</strong>: List of Python packages required to run the project.</li>
        </ul>

        <h2>Example Commands</h2>
        <ul>
            <li>"What is the weather today?"</li>
            <li>"Tell me a joke."</li>
            <li>"Set a reminder for 5 PM."</li>
            <li>"What is the capital of France?"</li>
            <li>"Exit" to quit the assistant.</li>
        </ul>

        <h2>Known Issues</h2>
        <ul>
            <li><strong>Network Dependency</strong>: Requires a stable internet connection to communicate with APIs.</li>
            <li><strong>Voice Model Selection</strong>: Make sure to select an appropriate voice ID from Eleven Labs that suits your needs.</li>
        </ul>

        <h2>Contributing</h2>
        <p>Feel free to open issues or submit pull requests for features, improvements, or bug fixes. Contributions are always welcome.</p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

        <h2>Acknowledgments</h2>
        <ul>
            <li><strong>Anthropic</strong> for the natural language processing capabilities.</li>
            <li><strong>Eleven Labs</strong> for providing state-of-the-art text-to-speech voices.</li>
            <li>The open-source community for inspiration and guidance.</li>
        </ul>
    </div>
</body>
</html>

