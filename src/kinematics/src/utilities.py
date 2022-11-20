import rospy
import math
import numpy as np
from std_srvs.srv import Empty
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SpawnModel, GetModelState, SetModelState

def spawn_coke_can(name, pose):
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)
    with open("/home/minc/gazebo_models/coke_can/model.sdf","r") as f:
        model_xml = f.read()
    spawn_model(name, model_xml, "", pose, "world")

def spawn_table(name, pose):
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)
    with open("/home/minc/gazebo_models/table/model.sdf", "r") as f:
        model_xml = f.read()
    spawn_model(name, model_xml, "", pose, "world")

def set_model_state(name, pose):
    rospy.wait_for_service("/gazebo/set_model_state")
    set_model_state_service = rospy.ServiceProxy("/gazebo/set_model_state", SetModelState)
    new_model_state = ModelState()
    new_model_state.model_name = name
    new_model_state.pose = pose
    set_model_state_service(new_model_state)

def get_model_state(name):
    rospy.wait_for_service("/gazebo/get_model_state")
    get_model_state_service = rospy.ServiceProxy("/gazebo/get_model_state", GetModelState)
    return get_model_state_service(name, "world")

