#! /usr/bin/env python3

import rospy
import math
from std_msgs.msg import Float64

def main():
    while not rospy.is_shutdown():
        #### |r| <= 4 
        # r < 0 : turn left
        # r > 0 : turn right
        
        r = -4
        if(r < -4): r = -4
        elif(r > 4): r = 4
        
        angle1 = math.degrees(math.atan(1.2/(r + 0.83)))
        angle2 = math.degrees(math.atan(1.2/(r - 0.83)))
        
        CmdPublish(angle1, angle2, 10, 10, 10, 10)

def CmdPublish(sl, sr, fl, fr, bl, br):
    front_left_steer.publish(Float64(-math.radians(sl)))
    front_right_steer.publish(Float64(-math.radians(sr)))
    front_left_wheel.publish(Float64(fl))
    front_right_wheel.publish(Float64(fr))
    back_left_wheel.publish(Float64(bl))
    back_right_wheel.publish(Float64(br))

if __name__=="__main__":
    rospy.init_node("ControlNode")
    front_left_wheel = rospy.Publisher("/robot/front_left_wheel_velocity_controller/command", Float64, queue_size = 10)
    front_right_wheel = rospy.Publisher("/robot/front_right_wheel_velocity_controller/command", Float64, queue_size = 10)
    front_left_steer = rospy.Publisher("/robot/left_steer_position_controller/command", Float64, queue_size = 10)
    front_right_steer = rospy.Publisher("/robot/right_steer_position_controller/command", Float64, queue_size = 10)
    back_left_wheel = rospy.Publisher("/robot/left_wheel_velocity_controller/command", Float64, queue_size = 10)
    back_right_wheel = rospy.Publisher("/robot/right_wheel_velocity_controller/command", Float64, queue_size = 10)
    main()