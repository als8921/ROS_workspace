#!/usr/bin/env python3
import rospy
from my_pkg.srv import *

def handle(req):
    print(f"Returning {req.a} + {req.b}")
    return AddTwoIntsResponse(req.a + req.b)

def server():
    rospy.init_node("Add_Two_Ints_Server")
    rospy.Service("add_two_ints", AddTwoInts, handle)
    print("서버 준비됨")
    rospy.spin()

if __name__=="__main__":
    server()