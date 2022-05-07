# Tossingbot Experiments

The current script is a demo showing joint position control and velocity control. It rotates around shoulder pan joint and then through velocity control moves shoulder lift joint and elbow joint( our prime joint using which we want to throw projectiles ).

I wish to add KDL inverse kinematics control so that it can automatically reach cartesian position 1 to cartesian position 2. Again Im not using moveit here. I will update this once I have KDL inverse kinematics script running.
In future I can also experiment control using dq/dt method using only velocity control and no position control as explained in report and presentation.

In order to run this file, you may reqire to install universal robots repo.
/home/gaurav/Videos/Screencast from 05-07-2022 02:28:41 AM.webm
