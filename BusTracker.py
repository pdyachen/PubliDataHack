from urllib.request import urlopen
from xml.etree.ElementTree import parse
import time
import webbrowser

DavesLatitude = 41.980262
DavesLongitude = -87.668452

def CheckDistance(lat1,lat2):
	return abs(69 * (lat1 - lat2))
	pass

def Monitor():

	ResultXml = 'PdaBus.xml'
	u = urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
	data = u.read()
	f = open(ResultXml, 'wb')
	f.write(data)
	f.close()

	doc = parse(ResultXml)
	for bus in doc.findall('bus'):
		dir = bus.findtext('dd')
		lon = float(bus.findtext('lon'))
		lat = float(bus.findtext('lat'))
		if dir == 'Northbound' and lat >= DavesLatitude:
			distance = CheckDistance(lat,DavesLatitude)
			print(bus.findtext('id'),dir,lat,distance)			
			if distance <= 0.5:
				webbrowser.open('http://maps.googleapis.com/maps/api/staticmap?size=2000x2000&sensor=false&markers=|%f,%f' % (lat, lon))
				pass			
			pass
		pass
	pass


while True:
    Monitor()
    time.sleep(20)


