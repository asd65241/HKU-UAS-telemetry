from dronekit import connect, VehicleMode
import time 

class Drone:
    # Connect to the Vehicle. 
    # Input: UDP/TCP endpoint
    # Output: Vehicle object
    def __init__(self):
        self.lat = None
        self.lon = None
        self.alt = None
        self.connection_string = None

    def connection(self, connection_string):
        self.connection_string = connection_string
        print("Connecting to vehicle on: %s" % (connection_string,))
        self.drone = connect(connection_string, wait_ready=True)

    def get_gps(self):
        self.lat = self.drone.location.global_relative_frame.lat
        self.lon = self.drone.location.global_relative_frame.lon
        self.alt = self.drone.location.global_relative_frame.alt
        print("lat, lon, alt: %s" % self.lat, self.lon, self.alt)

        return [self.lat, self.lon, self.alt]

    def disconnection(self):
        self.drone.close()
        print("Vehicle has been disconnected")



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
