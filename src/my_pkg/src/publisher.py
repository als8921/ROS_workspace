#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node("Publisher")
pub = rospy.Publisher("/counter", Int32, queue_size = 1)
rate = rospy.Rate(0.5)

count = Int32()
count.data = 0

while not rospy.is_shutdown():
    print(count, "Published")
    pub.publish(count)
    count.data += 1
    rate.sleep()