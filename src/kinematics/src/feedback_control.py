import rospy, math, numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class VelocityController():
    def __init__(self, topic):
        self.cmd_vel = rospy.Publisher(topic, Twist, queue_size=10)
        rospy.sleep(0.1)

    def move(self, linear_velocity=0.0, angular_velocity=0.0):
        msg = Twist()
        msg.linear.x = linear_velocity
        msg.angular.z = angular_velocity
        self.cmd_vel.publish(msg)

class OdometryReader():
    def __init__(self, topic):
        self.odom_pose = {}
        self.trajectory = []
        self.topic = topic
        self.subscribe()

    def callback(self, msg):
        self.odom_pose['x'] = msg.pose.pose.position.x
        self.odom_pose['y'] = msg.pose.pose.position.y
        self.trajectory.append((self.odom_pose['x'], self.odom_pose['y']))
        (_, _, self.odom_pose['theta']) = euler_from_quaternion([msg.pose.pose.orientation.x, 
                                                            msg.pose.pose.orientation.y, 
                                                            msg.pose.pose.orientation.z, 
                                                            msg.pose.pose.orientation.w])
    def subscribe(self):
        self.odom_subscriber = rospy.Subscriber(self.topic, Odometry, self.callback)
        rospy.sleep(0.1)

    def unregister(self):
        np.save('trajectory',self.trajectory)
        self.odom_subscriber.unregister()

def normalize(angle):
    angle = (angle + math.pi) % (2*math.pi) - math.pi
    return angle

rospy.init_node('kinematic_controller', anonymous=True)

##### Test Normalize #####
# import random
# for _ in range(10):
#     angle = (random.random()-0.5)*2*math.pi
#     new_angle = angle + (random.randint(0,10)-5) * 2*math.pi
#     norm_angle = normalize(new_angle)
#     print('%9.4f %9.4f %9.4f' %(angle, new_angle, norm_angle))
#####

def go_to(xg, yg, thetag_degrees):
    rho = float("inf")
    thetag = math.radians(thetag_degrees)
    while rho>0.01:
        rho = math.hypot(xg - odometry.odom_pose['x'], yg - odometry.odom_pose['y'])
        # thetag = odometry.odom_pose['theta']
        alpha = -odometry.odom_pose['theta'] + math.atan((yg - odometry.odom_pose['y'])/(xg - odometry.odom_pose['x']))
        beta = -thetag - alpha
        # print(math.degrees(thetag), math.degrees(alpha), math.degrees(beta), odometry.odom_pose['x'], odometry.odom_pose['y'])
        v = k_rho * rho
        w = k_alpha*alpha + k_beta * beta
        velocity.move(v, w)
        rospy.sleep(0.01)
        
k_rho = 0.3
k_alpha = 0.8
k_beta = -0.15


velocity = VelocityController('/cmd_vel')
odometry = OdometryReader('/odom')

waypoints = [(1,-1,-90),(2,-2,0),(3,-2,0),(4,-1,90),(3.5,-0.5,180),
             (3,0,90),(3,1,90),(2,1,-90),(1,0,180),(0,0,180)]

for xg, yg, thetag in waypoints:
    go_to(xg, yg, thetag)

velocity.move(0,0)
odometry.unregister()
error = math.hypot(odometry.odom_pose['x'], odometry.odom_pose['y'])
print('Final positioning error is %.2fm' % error)