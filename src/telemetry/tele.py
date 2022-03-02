from dronekit import connect, VehicleMode
import time 

class Drone:
    # Connect to the Vehicle. 
    # Input: UDP/TCP endpoint
    # Output: Vehicle object
    def __init__(self):
        self.battery_max_voltage = 16.8
        self.connection_string = None

    def connection(self, connection_string):
        self.connection_string = connection_string
        print("Connecting to vehicle on: %s" % (connection_string,))
        self.drone = connect(connection_string, wait_ready=True)

    def get_gps(self):
        lat = self.drone.location.global_relative_frame.lat
        lon = self.drone.location.global_relative_frame.lon
        alt = self.drone.location.global_relative_frame.alt

        return {"lat": lat, "lon": lon, "alt": alt, "heading": self.drone.heading, "ground_speed": drone.groundspeed}

    def get_battery(self):
        return {"battery": self.drone.battery}

    def get_battery_level(self):
        if current_voltage < full_voltage:
            current_voltage = self.drone.battery.voltage
            full_voltage = self.battery_max_voltage
            return {"battery_level": now/full}
        else:
            return {"battery_level": "N/A"}

    def get_status(self):
        return {"flight_mode": self.drone.mode.name, "system_status": self.drone.system_status.state, "isArmable": self.drone.is_armable, "isArmed": self.drone.armed}

    def get_dash(self):

        dash = {
            "gps": self.get_gps(),
            "battery_level": self.get_battery_level(),
            "status": self.get_status()
        }

        return dash

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

# # 飛控軟件版本
# print "Autopilot Firmware version: %s" % vehicle.version
# # 全球定位信息（經緯度，高度相對於平均海平面）
# print "Global Location: %s" % vehicle.location.global_frame
# # 全球定位信息（經緯度，高度相對於home點）
# print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
# # 相對home點的位置信息（向北、向東、向下）；解鎖之前返回None
# print "Local Location: %s" % vehicle.location.local_frame
# # 無人機朝向（歐拉角：roll，pitch，yaw，單位為rad，範圍-π到+π）
# print "Attitude: %s" % vehicle.attitude
# # 三維速度（m/s）
# print "Velocity: %s" % vehicle.velocity
# # GPS信息
# print "GPS: %s" % vehicle.gps_0
# # 地速（m/s）
# print "Groundspeed: %s" % vehicle.groundspeed
# # 空速（m/s）
# print "Airspeed: %s" % vehicle.airspeed
# # 雲台信息（得到的為當前目標的roll, pitch, yaw，而非測量值。單位為度）
# print "Gimbal status: %s" % vehicle.gimbal
# # 電池信息
# print "Battery: %s" % vehicle.battery
# # EKF（拓展卡曼濾波器）狀態
# print "EKF OK?: %s" % vehicle.ekf_ok
# # 超聲波或激光雷達傳感器狀態
# print "Rangefinder: %s" % vehicle.rangefinder
# # 無人機朝向（度）
# print "Heading: %s" % vehicle.heading
# # 是否可以解鎖
# print "Is Armable?: %s" % vehicle.is_armable
# # 系統狀態
# print "System status: %s" % vehicle.system_status.state
# # 當前飛行模式
# print "Mode: %s" % vehicle.mode.name
# # 解鎖狀態
# print "Armed: %s" % vehicle.armed