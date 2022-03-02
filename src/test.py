# Tests your package

__author__ = "you"
__email__ = "your email"

import unittest
import time
import dronekit_sitl
from telemetry import Drone

"""

To get your connection string, do

ls /dev/tty*.* 

"""

# Test code
drone = Drone()
drone.connection("/dev/tty.usbmodem01")

while True:
    # gps = drone.get_gps()
    # print(gps)

    # # Battery
    # battery_status = drone.get_battery_level()
    # print(battery_status)

    # # Status
    # status = drone.get_status()
    # print(status)

    print(drone.drone.heading)

    time.sleep(1)
