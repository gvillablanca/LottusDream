import requests

api_key = "AIzaSyDcO88A-VZWT28ICp5suDi6eKFUVN_8CrQ" 
url = "https://maps.googleapis.com/maps/api/staticmap?"
center = "Santiago"

zoom = 10
url_final = url + "center=" + center + "&zoom=" + str(zoom) + "&size=800x800&key=" + api_key + "&sensor=false"
r = requests.get(url_final) 
f = open('map.png', 'wb')
f.write(r.content) 
f.close()