from flask import Flask, request, jsonify

app = Flask(__name__)

locations = []  # List to store locations
location_id = 0  # Unique ID for each location

@app.route('/save_location', methods=['POST'])
def save_location():
    global location_id
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    location_id += 1
    locations.append({"id": location_id, "latitude": latitude, "longitude": longitude})
    
    return jsonify({"message": "Location saved successfully!"})

@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)
