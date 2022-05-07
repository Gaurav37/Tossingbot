#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray, Float64
import time
from controller_manager_msgs.srv import SwitchController

# To run this file:

# roslaunch gazebo_ros empty_world.launch
# rosrun gazebo_ros spawn_model -file `rospack find ur5-joint-position-control`/urdf/ur5_jnt_pos_ctrl.urdf -urdf -x 0 -y 0 -z 0.1 -model ur5
# roslaunch ur5-joint-position-control ur5_joint_position_control.launch
# rosrun ur5-joint-position-control trajectory_command.py
# rosservice call /controller_manager/list_controllers


rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1)

joint_com_pub0 = rospy.Publisher('/shoulder_pan_joint_position_controller/command', Float64, queue_size=50)
joint_com_pub1 = rospy.Publisher('/shoulder_lift_joint_position_controller/command', Float64, queue_size=50)
joint_com_pub2 = rospy.Publisher('/elbow_joint_position_controller/command', Float64, queue_size=50)
joint_com_pub3 = rospy.Publisher('/wrist_1_joint_position_controller/command', Float64, queue_size=50)
joint_com_pub4 = rospy.Publisher('/wrist_2_joint_position_controller/command', Float64, queue_size=50)
joint_com_pub5 = rospy.Publisher('/wrist_3_joint_position_controller/command', Float64, queue_size=50)


angle= Float64()
angle.data= 0.5
ctrl_c= False
while not ctrl_c:
    connections0 = joint_com_pub0.get_num_connections()
    connections1= joint_com_pub1.get_num_connections()
    connections2= joint_com_pub2.get_num_connections()
    connections3= joint_com_pub3.get_num_connections()
    connections4= joint_com_pub4.get_num_connections()
    connections5= joint_com_pub5.get_num_connections()
    if connections0 > 0 and connections1 >0 and connections2 >0 and connections3 >0 and connections4 >0 and connections5>0:
        joint_com_pub0.publish(angle)
        angle.data=0
        joint_com_pub1.publish(angle)
        joint_com_pub2.publish(angle)
        joint_com_pub3.publish(angle)
        joint_com_pub4.publish(angle)
        joint_com_pub5.publish(angle)
        ctrl_c = True
        rospy.sleep(rospy.Duration(10))
    else:
        rate.sleep()

rospy.wait_for_service('/controller_manager/switch_controller')
try:
   switch_controller = rospy.ServiceProxy('/controller_manager/switch_controller', SwitchController)
   ret = switch_controller(['joint_motor_controller', 'joint_state_controller'],
   ['shoulder_pan_joint_position_controller', 'shoulder_lift_joint_position_controller',
   'elbow_joint_position_controller', 'wrist_1_joint_position_controller', 'wrist_2_joint_position_controller',
   'wrist_3_joint_position_controller'], 0, False,0.0)
except rospy.ServiceException as e:
    print("Service call failed: " + str(e))

pub = rospy.Publisher('/joint_motor_controller/command', Float64MultiArray, queue_size=10)
rate = rospy.Rate(1) # 10hz

my_msg = Float64MultiArray()

data = [0,-3,-6,0,0,0]
my_msg.data = data
ctrl_c = False

while not ctrl_c:
    connections = pub.get_num_connections()
    if connections > 0:
        pub.publish(my_msg)
        rospy.sleep(rospy.Duration(0.3))
        data1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        my_msg.data = data1
        pub.publish(my_msg)
        ctrl_c = True
        # rospy.sleep(rospy.Duration(10))
    else:
        rate.sleep()
