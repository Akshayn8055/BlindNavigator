import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1.0)  # Max volume
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Change index for a different voice

def generate_audio(text, filename="response.wav"):
    """
    Converts text to speech and saves it as an audio file.

    Args:
        text (str): The text to convert into speech.
        filename (str): Output audio file name.

    Returns:
        str: Path to the generated audio file.
    """
    output_path = os.path.join("audio_responses", filename)
    
    # Ensure the directory exists
    os.makedirs("audio_responses", exist_ok=True)

    # Generate speech
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    return output_path

def speak(text):
    """
    Directly speaks the provided text without saving an audio file.

    Args:
        text (str): The text to be spoken aloud.
    """
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Audio feedback system is working correctly.")
    audio_file = generate_audio("This is a test response for blind navigation.")
    print("Audio file generated:", audio_file)
