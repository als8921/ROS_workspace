# CNU CAD/CAM

# Installization
## Ros Noetic Package
```bash
sudo apt install ros-noetic-joy ros-noetic-teleop-twist-joy ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc ros-noetic-rgbd-launch ros-noetic-depthimage-to-laserscan ros-noetic-rosserial-python ros-noetic-rosserial-server ros-noetic-rosserial-client ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro ros-noetic-compressed-image-transport ros-noetic-rqt-image-view ros-noetic-gmapping ros-noetic-navigation
```

```bash
cd
git clone https://github.com/als8921/ROS_workspace.git
```

```bash
cd ~/ROS_workspace
catkin_make
```

```bash
source ROS_workspace/devel/setup.bash
```

# HW2

```bash
roslaunch turtlebot3_gazebo turtlebot3_stage_3.launch 
roslaunch teleop_pkg auto.launch
```

