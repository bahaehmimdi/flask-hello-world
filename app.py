from flask import Flask, request,render_template
from flask import jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
active= {}  
locations = {}  # List to store locations
location_id = 0  # Unique ID for each location
rings=[]
@app.route('/save_location', methods=['POST'])
def save_location():
 try:   
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
 except Exception as err:
     return str(err)
@app.route('/get_locations', methods=['GET'])
def get_locations():
 try:   
   name = request.args.get('name')  # 'Guest' is the default value if 'name' is not provided
   if not name:
       return jsonfy([])
   localisation_copy=[]+locations
   if name in active.keys(): 
    localisation_copy.extend(active[name])
   try: 
    return jsonify(localisation_copy)
   except Exception as me:
       return str(me)
 except Exception as mee:
     return str(mee)
@app.route('/')
def index():
   try: 
    return render_template('map.html', locations=locations)
   except Exception as me:
       return str(me)
if __name__ == '__main__':
    app.run(debug=True)
