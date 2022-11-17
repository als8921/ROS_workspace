import math, rospy
from turtle import position
from utilities import get_model_state, set_model_state, spawn_wall
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

def set_wall():
    with open("/home/minc/gazebo_models/grey_wall/model.sdf","r") as f:
        model = f.read()
    q = quaternion_from_euler(0, 0, math.radians(90))
    spawn_wall(model, "g0", Pose(position = Point(10, 0, 0), orientation = Quaternion(*q)))
    spawn_wall(model, "g1", Pose(position = Point(10, 6.35, 0), orientation = Quaternion(*q)))
    spawn_wall(model, "g2", Pose(position = Point(10, -6.35, 0), orientation = Quaternion(*q)))
    spawn_wall(model, "g3", Pose(position = Point(0, 10, 0)))
    spawn_wall(model, "g4", Pose(position = Point(6.35, 10, 0)))
    spawn_wall(model, "g5", Pose(position = Point(-6.35, 10, 0)))
    spawn_wall(model, "g6", Pose(position = Point(-10, 0, 0), orientation = Quaternion(*q)))
    spawn_wall(model, "g7", Pose(position = Point(-10, 6.35, 0), orientation = Quaternion(*q)))
    spawn_wall(model, "g8", Pose(position = Point(-10, -6.35, 0), orientation = Quaternion(*q)))
    spawn_wall(model, "g9", Pose(position = Point(0, -10, 0)))
    spawn_wall(model, "g10", Pose(position = Point(6.35, -10, 0)))
    spawn_wall(model, "g11", Pose(position = Point(-6.35, -10, 0)))

def set_obstacle():
    with open("/home/minc/gazebo_models/number1/model.sdf","r") as f:
        model = f.read()
    spawn_wall(model, "ob0", Pose(position = Point(2.5, 2.5, 0.4)))
    spawn_wall(model, "ob1", Pose(position = Point(2.5, -2.5, 0.4)))
    spawn_wall(model, "ob2", Pose(position = Point(-2.5, 2.5, 0.4)))
    spawn_wall(model, "ob3", Pose(position = Point(-2.5, -2.5, 0.4)))
    spawn_wall(model, "ob_m0", Pose(position = Point(7.5, 2.5, 0.4)))
    spawn_wall(model, "ob_m1", Pose(position = Point(2.5, -7.5, 0.4)))
    spawn_wall(model, "ob_m2", Pose(position = Point(-7.5, -2.5, 0.4)))
    spawn_wall(model, "ob_m3", Pose(position = Point(-2.5, 7.5, 0.4)))

set_wall()
set_obstacle()


