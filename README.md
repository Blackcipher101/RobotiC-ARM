# RobotiC-ARM :mechanical_arm:
Ever seen arms in huge plants:factory:? Yes this is something like that which we a robotic manipulator in techincal terms and if I want to get more technical which I love(coz I brag:stuck_out_tongue_winking_eye:) that is
it's a 3DOF robot which basically means it has three joints that can move independently of each other something similar to a human arm a revolute joint followed by a continuous joint and another continuous joint.


# Comparsison :vs:


![](https://i.ibb.co/pnXSK5z/download-1.jpg) &nbsp;&nbsp;&nbsp;  <img src="https://i.ibb.co/Y8PfvwB/Screenshot-2021-05-04-22-00-32.png" height="260px">


# What does this arm do
So with this arm you can pick objects manually using a GUI other than that it uses forward :arrow_right: kinematics to print the end effector coordinates and using inverse kinematics :arrow_left: you can give a coordinate and the arm will align itself to that coordinate giving itself the desired joint values. This is a brief feature list the complete list of nodes is below

# Nodes
- tf
- joint_states
- joint_command
- forward kinematics
- inverse kinematics

# Tech and Tools ⚙️
The whole thing uses ROS Melodic which makes it really ease to builds nodes and communicate between the nodes. It has both rviz for static simltation and gazebo for dynamic physics sloutions you will see a use of ros-control to command the joints in gazebo

# Working

## Forward Kinematics

https://user-images.githubusercontent.com/33775493/117039182-1b1a4100-ad26-11eb-9716-c5116b786dc8.mp4

## Inverse Kinematics

https://user-images.githubusercontent.com/33775493/117039426-646a9080-ad26-11eb-94b2-2bc8f2e0e9d8.mp4







# How to run 🏃

Clone the repo
```
git clone <link>
```
Run ```catkin_make``` in both simulataion and catkin workspace
Then source the workspace
```
source devel/setup.bash
```
After this its just lauching the bot and the running the nodes
In simultation_ws
```
roslaunch gazebo_ros empty_world.launch
roslaunch arm_description spawn.launch
```
In catkin_ws
```
rosrun arm_move arm_move.py
```

# Contribution 👼
Feel free to make issues and contribute
