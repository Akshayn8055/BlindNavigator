from scene_description import describe_scene
from navigation import generate_navigation_instructions
from audio_feedback import speak
from audio_input import listen

def process_voice_command(detected_objects):
    """
    Listens for a voice command, processes it, and responds with useful information.

    Args:
        detected_objects (list): The current detected objects.

    Returns:
        str: Spoken response to the user.
    """
    command = listen()

    if "what" in command and "see" in command:  
        response = describe_scene(detected_objects)
    elif "where is" in command:
        object_name = command.split("where is")[-1].strip()
        found = [obj for obj in detected_objects if object_name in obj["label"]]

        if found:
            positions = []
            for obj in found:
                x1, _, x2, _ = obj["bbox"]
                center_x = (x1 + x2) / 2

                if center_x < 213:
                    positions.append(f"on your left")
                elif center_x > 426:
                    positions.append(f"on your right")
                else:
                    positions.append(f"directly in front of you")

            response = f"The {object_name} is {', '.join(positions)}."
        else:
            response = f"I don't see a {object_name} around you."

    elif "can I move" in command or "should I stop" in command:
        response = generate_navigation_instructions(detected_objects)
    
    else:
        response = "I'm not sure how to answer that."

    speak(response)
    return response

if __name__ == "__main__":
    # Test with sample objects
    sample_objects = [
        {"label": "chair", "bbox": [100, 200, 250, 400]},
        {"label": "table", "bbox": [300, 100, 500, 350]},
        {"label": "door", "bbox": [500, 50, 600, 200]}
    ]
    process_voice_command(sample_objects)
