#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("TwistPublish")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)

twist = Twist()
twist.linear.x = 0.5
twist.angular.z = 0.5

while not rospy.is_shutdown():
    print(twist)
    pub.publish(twist)