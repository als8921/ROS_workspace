#! /usr/bin/env python3

import rospy
import math
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node("AUTO")

twist = Twist()

def callback(data):
    ld = [0] * 9
    for i in range(0, 9):
        ld[i] = min(data.ranges[i * 80 :(i + 1) * 80])
    theta = 90-((np.argmax(ld)+1) * 20 - 10)
    twist.linear.x = 0.5
    twist.angular.z = -math.radians(theta) * 2

    print(theta)
    if any(i < 1 for i in ld):
        twist.linear.x = -0.5
        twist.angular.z = math.radians(theta) * 2



    # twist.linear.x = 0.5
    # twist.angular.z = 0

    pub.publish(twist)
    
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
rospy.Subscriber("/laser/scan", LaserScan, callback)
rospy.spin()