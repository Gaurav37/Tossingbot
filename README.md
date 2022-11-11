# Tossingbot Experiments
This project is inspired from [Google's tossingbot](https://tossingbot.cs.princeton.edu/paper.pdf). In the original method they train a deep learning model to learn the throw velocity of an object based on grasping pose, target position and the position it lands after throw. Keeping scope of timeline into mind I have focused on just pick and throw part.

Also there are many programmer friendly manipulator arms available in market like Kinect but for throwing we need speed and for that reason UR5 was selected.
At first I just tried to implement pick and place and then for velocity control and then I tried different config files and different controllers and finally with joint_group_velocity_controller I was able to control arm joint velocity as can be seen in below 2 videos for slow and fast velocities.

https://user-images.githubusercontent.com/19994641/196595095-59f4c03c-40ac-4674-ab55-d96e0e965ddb.mp4


https://user-images.githubusercontent.com/19994641/196595136-1954a252-dcd1-4fd1-adf7-8c976aaeae1a.mp4

Then my plan was to control all arm movements with velocity controller and I tried to write RRT from scratch and control arm using RRT but with differentail velocity method, however there were problems related to cspace.
Also I found that although joint_group_velocity_control worked through command line rostopic publishing it gave some problem if I tried to do it through python program. So after alot of experimentation finally I found sweet spot of another velocity controller and instead of controlling arm movement completely through velocity controller(using RRT), it seemed a better option to use multiple controllers so then I used joint position controller and velocity controller both for position control and velocity control respectively. Ofcourse I used switch controller mechanism.

https://user-images.githubusercontent.com/19994641/167242326-bed3da44-4e2a-461c-a291-e9226321722d.mp4


https://user-images.githubusercontent.com/19994641/196595255-65a53455-0711-4ba8-aeca-99464495662d.mp4
