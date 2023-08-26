from flask import Flask, request, jsonify

app = Flask(__name__)

locations = {}  # List to store locations
location_id = 0  # Unique ID for each location

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
    
    return "ringing"#jsonify({"message": "Location saved successfully!"})

@app.route('/get_locations', methods=['GET'])
def get_locations():
   try: 
    return jsonify(locations)
   except Exception as me:
       return str(me)
@app.route('/')
def bonjour():
    return "Bonjour c est bahae el hmimdi le devlopeur" +str(locations)
if __name__ == '__main__':
    app.run(debug=True)
