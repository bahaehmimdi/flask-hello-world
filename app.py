from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)

locations = {}  # List to store locations
location_id = 0  # Unique ID for each location
rings=[]
@app.route('/save_location', methods=['POST'])
def save_location():
    global location_id
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    name = data.get('name')
   # ring = data.get('ring')

    location_id += 1
    locations[name]={"id": location_id, "latitude": latitude, "longitude": longitude,"name":name}

    if name in rings:
     return "ringing"#jsonify({"message": "Location saved successfully!"})
    else:
     return ""   
@app.route('/get_locations', methods=['GET'])
def get_locations():
   name = request.args.get('name', 'toadd')  # 'Guest' is the default value if 'name' is not provided
   if name=="toadd":
       return jsonfy([])
   localisation_copy=[]+locations
   if name in active.keys(): 
    localisation_copy.extend(active[name])
   try: 
    return jsonify(localisation_copy)
   except Exception as me:
       return str(me)
@app.route('/')
def index():
    return render_template('map.html', locations=locations)

if __name__ == '__main__':
    app.run(debug=True)
