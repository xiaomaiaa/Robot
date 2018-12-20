#!/bin/bash
# source ~/catkin_ws/devel/setup.bash

#you only need to change the junk_cnt
junk_cnt=10
launch_file="turtlebot3_junk_move.launch"
run_agent_file="agent_final.py"


{
gnome-terminal -t "core" -x bash -c "roscore"
}&

sleep 3s
{
gnome-terminal -t "launch" -x bash -c "roslaunch turtlebot3_gazebo $launch_file"
}&

sleep 6s
{
gnome-terminal -t "run_agent" -x bash -c "rosrun turtlebot3_gazebo $run_agent_file"
}&

for ((i=0; i < $junk_cnt; i++))
do
    {
    gnome-terminal -t "junk$i" -x bash -c "rosrun turtlebot3_gazebo junk_move$i.py"
    }&
done