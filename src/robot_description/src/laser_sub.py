#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    print(min(data.ranges))

rospy.init_node("Laser_Sub")
rospy.Subscriber("/laser/scan", LaserScan, callback)
rospy.spin()
