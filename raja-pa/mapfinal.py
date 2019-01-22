import urllib.request
import json
import requests
import speech
def route(destination):
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j = json.loads(r.text)
	lat = j['latitude']
	lon = j['longitude']
	city=j['city']
	print("You are at "+str(city))
	speech.say("You are at "+str(city))
	bingMapsKey = "Ah1ha8z7d6jaHFMiWaokDWkH_x1Uk733r1PrUFD5rEsbIJlAxXCkSeCkW7DVDh80"
	longitude = lon
	latitude = lat
	encodedDest = urllib.parse.quote(destination, safe='')
	routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(latitude) + "," + str(longitude) + "&wp.1=" + encodedDest + "&key=" + bingMapsKey
	request = urllib.request.Request(routeUrl)
	response = urllib.request.urlopen(request)

	r = response.read().decode(encoding="utf-8")
	result = json.loads(r)

	itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]
	for item in itineraryItems:
		print(item["instruction"]["text"])
		speech.say(item["instruction"]["text"])
if __name__=="__main__":
	route("Hyderabad")