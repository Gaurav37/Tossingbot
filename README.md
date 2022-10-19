# Tossingbot Experiments

The current script is a demo showing joint position control and velocity control. It rotates around shoulder pan joint and then through velocity control moves shoulder lift joint and elbow joint( our prime joint using which we want to throw projectiles ).

I wish to add KDL inverse kinematics control so that it can automatically reach cartesian position 1 to cartesian position 2. Again Im not using moveit here. I will update this once I have KDL inverse kinematics script running.
In future I can also experiment control using dq/dt method using only velocity control and no position control as explained in report and presentation.

Update: kdl program is ready but it doesn't work sometimes so trying to perfect it.

In order to run this file, you may reqire to install universal robots repo.

In below video arm rotates a little and then moves with very high velocity as we have specified.


https://user-images.githubusercontent.com/19994641/196595095-59f4c03c-40ac-4674-ab55-d96e0e965ddb.mp4


https://user-images.githubusercontent.com/19994641/196595136-1954a252-dcd1-4fd1-adf7-8c976aaeae1a.mp4


https://user-images.githubusercontent.com/19994641/167242326-bed3da44-4e2a-461c-a291-e9226321722d.mp4
