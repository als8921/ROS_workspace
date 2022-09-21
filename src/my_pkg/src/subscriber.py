#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(data):
    print(data.data, "Subscribed")


rospy.init_node("Subscriber")

rospy.Subscriber("/counter", Int32, callback)
rospy.spin()

