把test.urdf.xacro与test.gazebo.xacro放到turtlebot3_description/urdf中
把test2.world放到turtlebot3_gazebo/worlds中
把turtlebot3_junk.launch放到turtlebot3_gazebo/launch中
运行roscore; 运行roslaunch turtlebot3_gazebo turtlebot3_junk.launch可以看到三个junk以及一个turtlebot3加载在没有墙壁的世界中。

【junk的朝向】打开turtlebot3_junk.launch，可以看到在first_tb3_yaw... ... third_tb3_yaw的default值分别为1.57,-1.57,1.57
注意，+1.57对应的x方向是向右，-1.57对应的x方向是向左（这里面的左右都是世界坐标系下的）

