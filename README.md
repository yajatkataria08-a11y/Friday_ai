# Friday: Python Voice Assistant

## Project Overview

**Friday** is a personal, modular, and extensible voice assistant inspired from marvel's,ironman assitant FRIDAY built entirely in Python. Designed for desktop use, it can automate common tasks, provide quick information, and control media playback using natural language commands.

Inspired by AI assistants in popular culture, Friday features a **wake word activation system** that ensures it only processes commands when you are ready.

## Features

* **Wake Word Activation:** Remains in a listening state until the user says the wake word: **"FRIDAY"**.
* **Intelligent Web Search:** Automatically constructs and executes Google searches based on commands like `"search for..."` or `"google..."`.
* **Web Automation:** Opens essential websites (YouTube, Google, Facebook, LinkedIn, GitHub, etc.) instantly in the default browser.
* **Local Music Player:** Features a dedicated **`music_handler`** module to select and play a random song from a local library upon hearing `"play music"`.
* **Contextual Information:** Provides real-time information, such as the current time, and answers basic introductory questions.
* **Dynamic Greetings:** Greets the user with "Good morning," "Good afternoon," or "Good evening" based on the time of day.

## Technologies & Tools Used

This project relies on the following Python libraries and system utilities:

| Technology | Purpose | Notes |
| :--- | :--- | :--- |
| **Python 3** | Core Programming Language | |
| **`speech_recognition`** | Transcribing spoken word into text commands. | Requires the **PyAudio** dependency. |
| **`pyttsx3`** | Text-to-Speech (TTS) engine for audio feedback. | |
| **`webbrowser`** | Controlling the system's default web browser. | Built-in Python module. |
| **`playsound`** | Playing local music files (used in `music_handler.py`). | |

## Steps to Install & Run the Project

### 1. Prerequisites (Crucial Step)

The `speech_recognition` library requires **PyAudio** to interact with your microphone. This is a common point of failure and may require specific dependencies depending on your operating system.

* **Windows:**
    ```bash
    pip install PyAudio
    ```
* **Linux (Ubuntu/Debian):**
    ```bash
    sudo apt-get install portaudio19-dev
    pip install PyAudio
    ```
* **macOS:**
    ```bash
    brew install portaudio
    pip install PyAudio
    ```

### 2. Setup and Dependencies

1.  **Clone the Repository (or download the files):**
    ```bash
    git clone [https://github.com/your-username/friday-voice-assistant.git](https://github.com/your-username/friday-voice-assistant.git)
    cd friday-voice-assistant
    ```

2.  **Install Required Python Libraries:**
    ```bash
    pip install SpeechRecognition pyttsx3 playsound
    ```

3.  **Setup the Music Library:**
    * Create a directory named **`music`** inside the project root folder.
    * Place your MP3 files inside this directory.
    * **Crucial:** Ensure the music file names in your `music_handler.py` match the actual files you placed in the `music` folder (e.g., `music/shakira_waka_waka.mp3`).

### 3. Run the Assistant

Start the voice assistant from your terminal:

```bash
python friday_assistant.py
