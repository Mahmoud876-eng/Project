from geopy.distance import geodesic

# Function to check if the person has left the geofence
def check_geofence_exit(user_location, safe_zone_location, safe_zone_radius):
    # Calculate the distance between the user and the safe zone
    distance = geodesic(user_location, safe_zone_location).meters
    
    # Check if the distance is greater than the safe zone radius
    if distance > safe_zone_radius:
        return True  # The person has left the safe zone
    else:
        return False  # The person is still inside the safe zone

# Example locations (latitude, longitude)
user_location = (40.421999, -122.084057)  # The tracked person's location
safe_zone_location = (37.421999, -122.084057)  # The center of the safe zone
safe_zone_radius = 100  # Safe zone radius in meters

# Check if the person has left the safe zone
if check_geofence_exit(user_location, safe_zone_location, safe_zone_radius):
    print("The person has left the safe zone!")
else:
    print("The person is still inside the safe zone.")
