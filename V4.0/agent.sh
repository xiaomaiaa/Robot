#!/bin/bash
 
# source ~/catkin_ws/devel/setup.bash
launch_file="turtlebot3_junk_move.launch"
run_file="agent_final.py"


{
gnome-terminal -t "core" -x bash -c "roscore"
}&

sleep 3s
{
gnome-terminal -t "launch" -x bash -c "roslaunch turtlebot3_gazebo $launch_file"
}&

sleep 6s
{
gnome-terminal -t "run" -x bash -c "rosrun turtlebot3_gazebo $run_file"
}&
