import google.generativeai as genai

# Load Gemini API Key (Replace with your actual API key)
GEMINI_API_KEY = "AIzaSyA4vOzZ6CFLvYdaMcEiIPSYuSgi3-6xTxs"  # 🔴 Do not share API keys publicly!
genai.configure(api_key=GEMINI_API_KEY)

def describe_scene(detected_objects):
    """
    Uses the Gemini API to generate a natural language scene description.

    Args:
        detected_objects (list): A list of detected objects with labels and positions.

    Returns:
        str: A human-friendly description of the scene.
    """
    if not detected_objects:
        return "No objects detected. The path seems clear."

    # Format object information into text
    object_text = ", ".join([obj["label"] for obj in detected_objects])

    # Create a prompt for Gemini
    prompt = f"Describe the scene to a blind person based on these objects: {object_text}. \
               Explain where they are positioned relative to the person, using simple language."

    try:
        # Call Gemini API with correct model name
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # ✅ Correct model name
        response = model.generate_content(prompt)

        # Extract text response safely
        if hasattr(response, 'text') and response.text:
            return response.text.strip()
        else:
            return "I couldn't generate a description."

    except Exception as e:
        print("❌ Error in scene description:", e)
        return f"There was an issue generating the scene description. ({str(e)})"

if __name__ == "__main__":
    # Test with sample data
    sample_objects = [
        {"label": "chair"},
        {"label": "table"},
        {"label": "door"}
    ]
    print(describe_scene(sample_objects))
