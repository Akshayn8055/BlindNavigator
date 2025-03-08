# AI Navigation Assistant

## Overview
The AI Navigation Assistant is designed to assist visually impaired individuals by providing real-time navigation guidance using object detection and audio feedback. The system consists of an Android application that streams camera frames to a server running a generalized object detection model. The server processes the frames, detects objects, and provides navigation instructions through an AI-powered voice assistant.

## Features
- **Object Detection:** Identifies objects in real time using a YOLO-based model.
- **Navigation Assistance:** Provides movement instructions based on detected obstacles.
- **Audio Feedback:** Converts text-based instructions into speech for user guidance.
- **GPS Integration:** Offers location-based assistance for outdoor navigation.
- **Voice Interaction:** Accepts voice commands for hands-free operation.

## System Architecture
### 1. Android Application
- Captures video frames and sends them to the server.
- Receives processed navigation instructions and provides audio feedback.
- Uses GPS for location tracking and route assistance.

### 2. Flask Server
- Hosts the object detection model.
- Processes incoming frames and generates navigation instructions.
- Sends responses back to the Android application.

### 3. AI Components
- Object detection model (YOLOv5).
- Text-to-speech module for generating voice output.
- Speech recognition module for voice-based interaction.

## Installation

### Prerequisites
- Python 3.8+
- Flask
- OpenCV
- PyTorch
- YOLOv5
- Pyttsx3 (for text-to-speech)
- Whisper (for speech recognition)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-navigation-assistant.git
   cd ai-navigation-assistant
