from flask import Flask, request,render_template, render_template_string
from flask import jsonify
from flask_socketio import SocketIO
import traceback
import pandas as pd
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
    ns=name.split("_")
    if len(ns)>2:
      name=ns[0]+"_"+ns[-2]+"_"+ns[-1]
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
       return jsonify([])
   localisation_copy={}
   for i,j in locations.items():
     if name in i: 
      localisation_copy[i]=j
   try: 
    return jsonify(localisation_copy)
   except Exception as me:
       return str(traceback.format_exc())
 except Exception as mee:
     return str(traceback.format_exc())
@app.route('/')
def index():
   try: 

    return render_template('map.html', locations=list(locations.values()))
   except Exception as me:
       return str(me)
@app.route('/l')
def indexl():
   try: 
    return jsonify({"locations": list(locations.values())})
   except Exception as me:
       return str(me)    
@app.route('/state')
def state():
   try: 
    name = request.args.get('name')
    if name in rings:
      rings.remove(name)
    else:
      rings.append(name)
    return "done" 
   except Exception as me:
       return str(me)    
@app.route('/completed')
def completed():
   try: 
    name = request.args.get('name')
    for i,j in locations.copy().items():
     if name in i and "cible" in i:
       del locations[i]
   except Exception as me:
       return str(me)   
@app.route('/datas')
def datas():
 try:
    # Fetch data from a URL (replace with your URL)
    ll=list(locations.values())
    for po,i in enumerate(ll.copy()):
      if i["name"] in rings:
        ll[po]["name"]="ringing"
      else: 
        ll[po]["name"]="not ringing"
    # Convert data to a DataFrame and then to an HTML table
    df = pd.DataFrame(list(locations.values()))
    html_table = df.to_html(classes='dataframe', border=1, index=False)
    
    return jsonify({'table': html_table}) 
 except Exception as me:
       return str(traceback.format_exc())
if __name__ == '__main__':
    app.run(debug=True)
