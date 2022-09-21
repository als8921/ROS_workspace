#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node("AUTO")

twist = Twist()

def callback(data):
    twist.linear.x = 0.1
    twist.angular.z = 0

    if(data.ranges[0] > 1): twist.linear.x = 0.2
    else: twist.angular.z = 0.5

    if(data.ranges[90] < 1): twist.angular.z = -0.5
    if(data.ranges[270] < 1): twist.angular.z = 0.5

    print(data.ranges[0], data.ranges[90], data.ranges[270])
    pub.publish(twist)
    
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
rospy.Subscriber("/scan", LaserScan, callback)
rospy.spin()