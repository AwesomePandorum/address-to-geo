import pandas as pd

df = pd.read_csv('locations.csv')
df


import googlemaps
gmaps_key = googlemaps.Client(key='AIzaSyAlLTmUbsK0IX_Lyk0BhyyXNIPA6j3ABKk')

df['LAT'] = None
df['LON'] = None

for i in range(0, len(df), 1):
    geocode_result = gmaps_key.geocode(df.iat[i, 0]
    try:
        lat = geocode_result[0]['geometry']['location']['lat']
        lon = geocode_result[0]['geometry']['location']['lng']
        df.iat[i, df.columns.get_loc('LAT')] = lat
        df.iat[i, df.columns.get_loc('LON')] = lon
    except:
        lat = None
        lon = None
