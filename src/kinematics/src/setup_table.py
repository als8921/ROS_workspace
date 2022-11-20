import math, rospy
from utilities import spawn_coke_can, spawn_table
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

spawn_table('table', Pose(position=Point(1,0,0)))
r = 0.2
for i in range(12):
    q = quaternion_from_euler(0, math.radians(90), math.radians(i*30))
    spawn_coke_can('coke_can_'+str(i), Pose(position=Point(1 + r*math.cos(math.radians(i * 30)), r*math.sin(math.radians(i * 30)),1.1), orientation=Quaternion(*q)))