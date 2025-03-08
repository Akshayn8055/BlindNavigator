def process_gps_data(gps_info):
    """
    Processes GPS coordinates and provides navigation feedback.

    Args:
        gps_info (dict): Contains 'latitude' and 'longitude'.

    Returns:
        str: Navigation message based on GPS data.
    """
    latitude = gps_info.get("latitude")
    longitude = gps_info.get("longitude")

    if latitude is None or longitude is None:
        return "Invalid GPS data received."

    # Example: Provide basic navigation guidance
    if latitude > 50.0:
        guidance = "You are in the northern region. Be aware of changing terrain."
    elif latitude < -50.0:
        guidance = "You are in the southern region. Navigation may require adjustments."
    else:
        guidance = "GPS signal received. Processing route information."

    return f"Received GPS coordinates: Latitude {latitude}, Longitude {longitude}. {guidance}"

if __name__ == "__main__":
    # Test with sample GPS data
    sample_gps = {"latitude": 12.9716, "longitude": 77.5946}  # Example coordinates (Bangalore)
    print(process_gps_data(sample_gps))
