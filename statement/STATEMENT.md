# Project Statement: Friday Voice Assistant

## Problem Statement

In today's fast-paced digital environment, users frequently interrupt their workflow to perform simple, repetitive tasks such as opening specific websites, searching the web, or controlling media playback. Constantly switching context between keyboard/mouse input and application interfaces reduces productivity and breaks concentration. There is a need for a seamless, hands-free interface to execute these common desktop actions efficiently using natural language.

## Scope of the Project

The scope of the Friday Voice Assistant project is to create a functional, modular, and easy-to-use desktop application that:

1.  **Handles Voice Input:** Reliably converts spoken commands into executable text commands using the microphone.
2.  **Implements a Wake Word:** Uses the word "Friday" to activate the command-listening state, minimizing accidental execution and promoting focused interaction.
3.  **Executes Core Functions:** Successfully executes commands related to web browsing, web search, media playback of local files, and system information retrieval.
4.  **Provides Audio Feedback:** Gives clear, verbal responses to confirm actions or deliver information.

The project is intentionally limited to common, pre-defined commands and does not include advanced features like file manipulation, deep system configuration, or complex API integrations (beyond standard web links).

## Target Users

The primary target users for the Friday Voice Assistant are:

* **Students and Professionals:** Individuals who frequently use the computer for research, coding, or communication and need a hands-free way to jump between applications and search engines.
* **Developers and Programmers:** Users who appreciate efficiency and wish to customize or extend the assistant's capabilities for their specific workflows.
* **Casual Desktop Users:** Anyone looking for a fun and engaging way to interact with their computer for basic tasks like checking the time or playing music.

## High-Level Features

1.  **Voice Interaction Layer:** Robust microphone input processing and accurate speech-to-text conversion.
2.  **Activation Logic:** A loop-based system that listens for the "Friday" wake word to transition into command mode.
3.  **Command Processor:** A comprehensive handler that maps recognized text commands to specific Python functions (e.g., `webbrowser.open()`, `music_handler.play_random_song()`).
4.  **TTS Response System:** Clear text-to-speech output for acknowledgments, greetings, and requested information.
5.  **Modular Music Handling:** A separate module (`music_handler.py`) for managing a local library and controlling playback, ensuring the main assistant script remains clean.
