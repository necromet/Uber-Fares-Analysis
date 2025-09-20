from math import radians, degrees, sin, cos, atan2, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
	# convert decimal degrees to radians
	lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
	# haversine formula
	dlat = lat2 - lat1
	dlon = lon2 - lon1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	r = 6371  # Radius of earth in kilometers
	return r * c

def calculate_bearing(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    diff_long = radians(lon2 - lon1)
    x = sin(diff_long) * cos(lat2)
    y = cos(lat1) * sin(lat2) - (sin(lat1) * cos(lat2) * cos(diff_long))
    init_bearing = atan2(x, y)
    init_bearing = degrees(init_bearing)
    comp_bearing = (init_bearing + 360) % 360
    return comp_bearing

# Calculate destination point given start point, bearing, and distance
def destination_point(lat1, lon1, distance_km, bearing_deg):
    r = 6371  # Earth radius in kilometers
    bearing = radians(bearing_deg)
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = asin(sin(lat1) * cos(distance_km / r) +
                cos(lat1) * sin(distance_km / r) * cos(bearing))
    lon2 = lon1 + atan2(sin(bearing) * sin(distance_km / r) * cos(lat1),
                        cos(distance_km / r) - sin(lat1) * sin(lat2))
    return degrees(lat2), degrees(lon2)