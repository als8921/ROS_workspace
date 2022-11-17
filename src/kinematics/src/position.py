import math, rospy
from turtle import position
from utilities import get_model_state, set_model_state, spawn_coke_can
from geometry_msgs.msg import Pose, Point, Quaternion

if get_model_state("coke_can").success == False:
    spawn_coke_can("coke_can", Pose(position = Point(0, 0, 0.5)))

