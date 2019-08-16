# This script converts a street address to coordinates using Google Geocoding API

import pandas as pd
import googlemaps

gmaps = googlemaps.Client(key='XXXXXXXXXXXXXXXXXXXX')

def geocoding_function(data):
	df = pd.DataFrame(data)

	for index, row in df.iterrows():
		# Taking the street address and city from the dataframe
	    street = row['street_address']
	    city = row['city']
	    address = street + ',' + city

	    # Passing the address field to Geocoding API and storing the latitude and longitude values in the dataframe
	    coordinates = gmaps.geocode(address)[0]['geometry']['location']
	    df.loc[index, 'Latitude'] = coordinates['lat']
	    df.loc[index, 'Longitude'] = coordinates['lng']

	return df


def get_output_schema():
	return pd.DataFrame({
		'id' : prep_int(),
		'street_address' : prep_string(),
		'city' : prep_string(),
		'Latitude' : prep_decimal(),
		'Longitude' : prep_decimal(),
		})