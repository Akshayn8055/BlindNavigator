def generate_navigation_instructions(detected_objects):
    """
    Generates movement instructions based on detected objects.

    Args:
        detected_objects (list): A list of detected objects with labels and bounding boxes.

    Returns:
        str: Navigation instructions for the user.
    """
    if not detected_objects:
        return "No obstacles detected. You can move forward safely."

    obstacles = []
    open_path = True

    for obj in detected_objects:
        label = obj["label"]
        x1, _, x2, _ = obj["bbox"]  # Extract bounding box (x-coordinates)
        center_x = (x1 + x2) / 2  # Get center position

        # Define general zones based on frame width (assuming 640px)
        if center_x < 213:  
            position = "on your left"
        elif center_x > 426:  
            position = "on your right"
        else:  
            position = "in front of you"
            open_path = False  # Blocked path

        obstacles.append(f"a {label} {position}")

    # Construct navigation instructions
    if open_path:
        instruction = "There are obstacles around, but the path ahead is clear. Move forward carefully."
    else:
        instruction = f"You should stop. There is {', '.join(obstacles)}. Try moving slightly left or right."

    return instruction

if __name__ == "__main__":
    # Test with sample data
    sample_objects = [
        {"label": "chair", "bbox": [100, 200, 250, 400]},  # Left side
        {"label": "table", "bbox": [300, 100, 500, 350]},  # Center
        {"label": "door", "bbox": [500, 50, 600, 200]}  # Right side
    ]
    print(generate_navigation_instructions(sample_objects))
