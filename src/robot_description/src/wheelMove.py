#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

rospy.init_node("WheelMoveNode")
pub = rospy.Publisher("/joint_states", JointState, queue_size = 10)
rate = rospy.Rate(10)
js = JointState()
js.name = ["joint_chassis_left_wheel"]
theta = 0
while not rospy.is_shutdown():
    if(theta > 3.14):
        theta = -3.14
    
    theta += 0.01
    js.position = [theta]
    print(js)
    pub.publish(js)
    rate.sleep()
