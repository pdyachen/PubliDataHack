from urllib.request import urlopen
from xml.etree.ElementTree import parse
import time
import webbrowser

DavesLatitude = 41.980262
DavesLongitude = -87.668452

def FindNorthBuses():
	result_xml = 'PdaBus.xml'
	u = urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
	data = u.read()
	f = open(result_xml, 'wb')
	f.write(data)
	f.close()
	north_buses = []
	doc = parse(result_xml)
	for bus in doc.findall('bus'):
		dir = bus.findtext('dd')
		lat = bus.findtext('lat')
		if dir == 'Northbound' and float(lat) > DavesLatitude:
			north_buses.append(bus.findtext('id'))
			pass	
		pass
	print(north_buses)	
	return north_buses
	pass

def CheckDistance(lat1,lat2):
	return abs(69 * (lat1 - lat2))
	pass

def Monitor(buses_to_track):
	result_xml = 'PdaBus.xml'
	u = urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
	data = u.read()
	f = open(result_xml, 'wb')
	f.write(data)
	f.close()	
	doc = parse(result_xml)	
	# print(buses_to_track)
	for bus in doc.findall('bus'):
		if bus.findtext('id') in buses_to_track:
			lon = float(bus.findtext('lon'))
			lat = float(bus.findtext('lat'))		
			distance = CheckDistance(lat,DavesLatitude)
			print(bus.findtext('id'),lat,distance)			
			if distance <= 0.5:
				webbrowser.open('http://maps.googleapis.com/maps/api/staticmap?size=2000x2000&sensor=false&markers=|%f,%f' % (lat, lon))
				buses_to_track.remove(bus.findtext('id'))
				pass
			pass
		pass
	pass
pass

north_buses = FindNorthBuses()	
while True:
    Monitor(north_buses)
    time.sleep(20)
    pass


