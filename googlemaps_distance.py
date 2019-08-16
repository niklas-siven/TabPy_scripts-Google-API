# This script calculates the walking distance from origin point to destination point included in the dataset using coordinates

import pandas as pd
import googlemaps

# Inserting the API key
gmaps = googlemaps.Client(key='XXXXXXXXXXXXXXXXXX')

def distance_function(data):
	df = pd.DataFrame(data)

	# Setting the Tableau London office coordinates as the origin
	latitude_origin='51.5062'
	longitude_origin='-0.0998'
	origin = (latitude_origin,longitude_origin)

	# Take the coordinates of each row, use the Google Distance Matrix API to calculate distances
	for i,Lat,Long in zip(df.index,df['Latitude'],df["Longitude"]):
		try:
			destination = (Lat,Long)
			distance = gmaps.distance_matrix(origin, destination, mode='walking')["rows"][0]["elements"][0]["distance"]["value"]
			df.at[i,'Distance'] = distance
		except:
			pass

	return df


# Defining the output schema for Prep
def get_output_schema():
	return pd.DataFrame({
		'Address' : prep_string(),
		'Latitude' : prep_decimal(),
		'Longitude' : prep_decimal(),
		'Distance': prep_int(),
		'Name' : prep_string(),
		'Price Level' : prep_int(),
		'Rating' : prep_decimal()
		})
