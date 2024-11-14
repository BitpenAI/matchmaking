from geopy.distance import geodesic

def calculate_distance(loc1, loc2):
    return geodesic(loc1, loc2).kilometers
