import dronekit_sitl
from dronekit import connect, VehicleMode
from pymavlink import mavutil
import time 


# SITL
print("Start simulator (SITL)")
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()



# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes (state)
print ("Get some vehicle attribute values:")
print (" GPS: %s" % vehicle.gps_0)
print (" Battery: %s" % vehicle.battery)
print (" Last Heartbeat: %s" % vehicle.last_heartbeat)
print (" Is Armable?: %s" % vehicle.is_armable)
print (" System status: %s" % vehicle.system_status.state)
print (" Mode: %s" % vehicle.mode.name)    # settable


# GPS data
print("Position: %s" % vehicle.location.global_relative_frame)
print("Latitude: %s" % vehicle.location.global_relative_frame.lat)
print("Longitude: %s" % vehicle.location.global_relative_frame.lon)
print("Altitude: %s" % vehicle.location.global_relative_frame.alt)


# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")