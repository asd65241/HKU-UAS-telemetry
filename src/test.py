# Tests your package

__author__ = "you"
__email__ = "your email"

import unittest
import time
import dronekit_sitl
from telemetry import connection, get_gps, disconnection

# SITL
print("Start simulator (SITL)")
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()


# Test code
drone1 = connection(connection_string)

for i in range(5):
    gps1 = get_gps(drone1)
    time.sleep(1)

print("last gps: %s" %gps1)

disconnection(drone1)




# Shut down simulator
sitl.stop()
print("Completed")