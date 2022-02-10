from dronekit import connect, VehicleMode
import time 

# Connect to the Vehicle. 
# Input: UDP/TCP endpoint
# Output: Vehicle object
def connection(connection_string):
    print("Connecting to vehicle on: %s" % (connection_string,))
    vehicle = connect(connection_string, wait_ready=True)

    return vehicle

def get_gps(vehicle):
    lat = vehicle.location.global_relative_frame.lat
    lon = vehicle.location.global_relative_frame.lon
    alt = vehicle.location.global_relative_frame.alt
    print("lat, lon, alt: %s" % lat, lon, alt)

    return [lat, lon, alt]

def disconnection(vehicle):
    vehicle.close()
    print("Vehicle has been disconnected.")




# Get some vehicle attributes (state)
# print ("Get some vehicle attribute values:")
# print (" GPS: %s" % vehicle.gps_0)
# print (" Battery: %s" % vehicle.battery)
# print (" Last Heartbeat: %s" % vehicle.last_heartbeat)
# print (" Is Armable?: %s" % vehicle.is_armable)
# print (" System status: %s" % vehicle.system_status.state)
# print (" Mode: %s" % vehicle.mode.name)    # settable
# print("Position: %s" % vehicle.location.global_relative_frame)
# print("Latitude: %s" % vehicle.location.global_relative_frame.lat)
# print("Longitude: %s" % vehicle.location.global_relative_frame.lon)
# print("Altitude: %s" % vehicle.location.global_relative_frame.alt)
