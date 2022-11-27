import rospy, math, numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

rospy.init_node('kinematic_controller', anonymous=True)

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


velocity = VelocityController('/cmd_vel')
odometry = OdometryReader('/odom')
rospy.sleep(1)

##### YOUR CODE STARTS HERE ##### 


##### YOUR CODE ENDS HERE ##### 
# # v = rw
# velocity.move(1,1) #w = 1 theta = pi/2
# rospy.sleep(math.pi/2)

# velocity.move(1,-1) #w = 1 theta = pi/2
# rospy.sleep(math.pi/2)

# velocity.move(5,0)
# rospy.sleep(1)

# velocity.move(5,-1) #w = 1 theta = pi/2
# rospy.sleep(math.pi/2)
v = 0.5
r = 5
# velocity.move(v, v/r)
# rospy.sleep(r* math.radians(90)/v)
velocity.move(v, -v/r)
rospy.sleep(r* math.radians(90)/v)
velocity.move(v, v/r)
rospy.sleep(r* math.radians(90)/v)
velocity.move(1, 0)
rospy.sleep(5)
velocity.move(v, v/r)
rospy.sleep(r* math.radians(90)/v)
r = 2.5
velocity.move(v, v/r)
rospy.sleep(r* math.radians(90)/v)
velocity.move(v, -v/r)
rospy.sleep(r* math.radians(90)/v)
velocity.move(1, 0)
rospy.sleep(5)
velocity.move(v, v/r)
rospy.sleep(r* math.radians(180)/v)
r = 5
velocity.move(v, -v/r)
rospy.sleep(r* math.radians(90)/v)
velocity.move(1, 0)
rospy.sleep(5)

velocity.move(0,0)
odometry.unregister()
error = math.hypot(odometry.odom_pose['x'], odometry.odom_pose['y'])
print('Final positioning error is %.2fm' % error)