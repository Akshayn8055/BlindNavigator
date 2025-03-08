import torch
import whisper
import sounddevice as sd
import numpy as np
import wave

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Whisper model (Use 'tiny', 'base', 'small', 'medium', or 'large')
model = whisper.load_model("medium").to(device)

# Recording settings
SAMPLE_RATE = 16000  # Whisper prefers 16kHz
CHANNELS = 1  # Mono audio
DURATION = 5  # Record for 5 seconds

def listen():
    """
    Captures voice input from the user, converts it to text using Whisper (offline, GPU).
    
    Returns:
        str: The recognized text from the user's speech.
    """
    print("Listening...")

    # Record audio from microphone
    audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=np.int16)
    sd.wait()  # Wait for recording to complete

    # Save to temp WAV file
    wav_file = "temp_audio.wav"
    with wave.open(wav_file, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data.tobytes())

    # Transcribe using Whisper (on GPU)
    result = model.transcribe(wav_file)
    
    return result["text"].strip().lower()

if __name__ == "__main__":
    print("You said:", listen())
