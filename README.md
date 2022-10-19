# Tossingbot Experiments

The current script is a demo showing joint position control and velocity control. It rotates around shoulder pan joint and then through velocity control moves shoulder lift joint and elbow joint( our prime joint using which we want to throw projectiles ).

I wish to add KDL inverse kinematics control so that it can automatically reach cartesian position 1 to cartesian position 2. Again Im not using moveit here. I will update this once I have KDL inverse kinematics script running.
In future I can also experiment control using dq/dt method using only velocity control and no position control as explained in report and presentation.

Update: kdl program is ready but it doesn't work sometimes so trying to perfect it.

In order to run this file, you may reqire to install universal robots repo.

In below video arm rotates a little and then moves with very high velocity as we have specified.

https://github.com/Gaurav37/Tossingbot/blob/70d01d3ba0f4327a0f64c9c28dd35d5c39127a34/Slow%20circle.mp4

https://github.com/Gaurav37/Tossingbot/blob/main/Fast%20Circle.mp4

https://user-images.githubusercontent.com/19994641/167242326-bed3da44-4e2a-461c-a291-e92

Uploading Slow circle.mp4…

26321722d.mp4
