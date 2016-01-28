from geopy.geocoders import Nominatim
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@socketio.on('hippo broadcast event', namespace='/test')
def broadcast_shipment_created(message):
    emit('shipment_created', 
    	{"to_location": [32.7174209 + random.uniform(1,13), -117.1627714 + random.uniform(1,44)], 
    	"from_location":[32.7174209 + random.uniform(1,13), -117.1627714 + random.uniform(1,44)]}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

def geolocate_address_string(address):
 	geolocator = Nominatim()
 	try:
 		location = geolocator.geocode(address)
 	except:
 		location = None
 	if location is not None:
 		return {"lat": location.latitude, "lng": location.longitude}

def dispatch():
	# first retrieve from and to address
	address_from_string = "1168 Folsom St. San Francisco CA 94107" # need to get that from Sumo!
	address_to_string   = "Nuernberger Str. 91, 91220 Schnaittach, Germany" # need to get that from Sumo!
	# geolocate them
	location_from = geolocate_address_string(address_from_string)
	location_to   = geolocate_address_string(address_to_string)
	# send them to broadcast
	# tbd


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
