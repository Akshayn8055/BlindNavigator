AI Multimodal Navigation Assistant for blind people
Overview
The AI Navigation Assistant is designed to assist visually impaired individuals by providing real-time navigation guidance using object detection and audio feedback. The system consists of an Android application that streams camera frames to a server running a generalized object detection model. The server processes the frames, detects objects, and provides navigation instructions through an AI-powered voice assistant.

Features
Object Detection: Identifies objects in real time using a YOLO-based model.
Navigation Assistance: Provides movement instructions based on detected obstacles.
Audio Feedback: Converts text-based instructions into speech for user guidance.
GPS Integration: Offers location-based assistance for outdoor navigation.
Voice Interaction: Accepts voice commands for hands-free operation.
System Architecture
Android Application

Captures video frames and sends them to the server.
Receives processed navigation instructions and provides audio feedback.
Uses GPS for location tracking and route assistance.
Flask Server

Hosts the object detection model.
Processes incoming frames and generates navigation instructions.
Sends responses back to the Android application.
AI Components

Object detection model (YOLOv5).
Text-to-speech module for generating voice output.
Speech recognition module for voice-based interaction.
Installation
Prerequisites
Python 3.8+
Flask
OpenCV
PyTorch
YOLOv5
Pyttsx3 (for text-to-speech)
Whisper (for speech recognition)
Setup
Clone the repository:

sh
Copy
Edit
git clone https://github.com/your-repo/ai-navigation-assistant.git
cd ai-navigation-assistant
Install dependencies:

sh
Copy
Edit
pip install -r requirements.txt
Start the Flask server:

sh
Copy
Edit
python main.py
Deploy the Android application on a device. Ensure the server and phone are on the same network.

Usage
Launch the Android application.
The application starts streaming camera frames to the server.
The server processes the frames and sends navigation instructions.
The application converts text instructions to speech for the user.
The user can give voice commands for additional assistance.
API Endpoints
Object Detection and Navigation
Endpoint: /process_frame

Method: POST
Description: Receives an image frame from the Android app, processes it, and returns navigation instructions.
Request Format:
json
Copy
Edit
{
  "image": "base64_encoded_frame"
}
Response Format:
json
Copy
Edit
{
  "instruction": "Move forward carefully. A chair is on your left."
}
Voice Command Processing
Endpoint: /audio_input

Method: POST
Description: Receives and processes voice commands.
Response Format:
json
Copy
Edit
{
  "response": "You are heading towards the exit."
}
Troubleshooting
API Not Responding
Ensure the Flask server is running.
Check that the Android app is using the correct server IP address.
Verify network connectivity between the phone and the server.
405 Method Not Allowed
Ensure the correct HTTP method is used (POST instead of GET).
Verify that the endpoint is correctly implemented in main.py.
No Audio Feedback
Confirm that the pyttsx3 module is installed.
Check the generated audio files for errors.
License
This project is licensed under the MIT License.
