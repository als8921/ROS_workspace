import math, rospy
from utilities import set_model_state, get_model_state
from geometry_msgs.msg import Pose, Point, Quaternion

model_state = get_model_state('my_robot')
position = Point(x=0, y=0, z=model_state.pose.position.z)
for angle in range(0,360,1):
    theta = math.radians(angle)
    orientation = Quaternion(x=0, y=0, z=math.sin(theta/2), w=math.cos(theta/2))
    set_model_state('my_robot', Pose(position, orientation))
    rospy.sleep(0.01)