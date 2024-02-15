import zmq
import json 
import requests
import csv

# Create a ZMQ context
context = zmq.Context()

socket = context.socket(zmq.REP)

# Pick 40000 + last three digits of your 900 ID
serverPort = 40639

URL = "http://ns-mn1.cse.nd.edu/sysprogfa23/assignment08/data/2019-01-21/0.json"

def load_default_data():
    # yoink the data we start off with 
    response = requests.get(URL)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Failed to fetch data from {URL}. Status code: {response.status_code}")
        exit()

def process_request(name_dict, name):
    # this will take in the name of the beacon and return the data in a csv format
    # if the name is not found, return FAILURE - Error Message
    if name in name_dict:
        #make it into string with commas
        return_string = ""
        return_string += name_dict[name][0] + ","
        return_string += name_dict[name][1] + ","
        return_string += name_dict[name][2] + ","
        return_string += name_dict[name][3]

        return return_string

    else:
        return "FAILURE - Beacon not found"
    
def send_response(response):
    socket.send_string(response)

# Load the default data
data = load_default_data()

#make a dict with the format name: [factory_id, battery_level, battery_updated_date, hardware]
name_dict = {}
for i in range(len(data)):
    name_dict[data[i]['name']] = [data[i]['factory_id'], 
                                  data[i]['battery_level'],
                                  data[i]['battery_updated_date'], 
                                  data[i]['hardware']]

#bind to port
try: 
    print('Starting up server on port ' + str(serverPort))
    socket.bind("tcp://*:" + str(serverPort))
except:
    print('Failed to bind on port ' + str(serverPort))
    exit()

while True:
    # Wait for a request from the client
    message = socket.recv_string()
    message = message.strip()
    #clean tf out of the message everything except letters numbers and dashes and parentheses
    message = ''.join(e for e in message if e.isalnum() or e == '-' or e == '(' or e == ')')
    #this was really annoying. Don't touch it. It might fail for certain inputs 
    print("Received request: " + message)
    
    # Process request and send response
    response = process_request(name_dict, message)
    print("Approptiate response sent") 
    
    send_response(response)

    
    