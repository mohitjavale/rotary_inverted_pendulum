# rotary_inverted_pendulum

This is a ros-noetic package that contains a gazebo simualtion environment for a rotary inverted pendulum.

## Launch sim

For launching sim - 
`roslaunch rotary_inverted_pendulum sim.launch`

## Communicating with the sim

To send commands to base actuator, publish Float64 msg on `/rotary_inverted_pendulum/Rev1_position_controller/command` topic.
To get info about robot joints, subscribe to `/rotary_inverted_pendulum/joint_states1` topic.
The rotory_joint (actuated) corresponds to the 0th index joint.
The pendulum_joint (free) corresponds to the 1st index joint.

## Changing +-45 constraint 

The pendulum joint is constrained to -45 to +45 from the desired topmost position for ease of testing and tweaking of controls.
You may stop this behaviour (enabling continuous free rotation) by chaning the joint type of joint "Rev2" from revoltue to continuous in the rotary_inverted_pendulum.xacro file. 

## Writing and launching your own scripts

For control algorithms, write code in the scripts folder, and run such as - `rosrun rotary_inverted_pendulum pid.py`
Sample for base pid is written.
Alongside this, a script to dynamicaly reconfigure the above pid is also written. This script can be run alongside the pid script, and shall open up a tkinter window, in which you can set custom pid values and see their outcome. The reset button sets all of the pid values to 0. The update button updates the pid values to those present on the slider.
