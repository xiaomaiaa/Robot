# Robot
先自己下载安装一个turtlebot3，学一下怎么运行  
在turtlebot3_simulations/turtle...gazebo/下，创建文件夹scripts，里边放入go.py文件  
在tur...gazebo文件夹中，打开CMakeLists.txt，给find_package()中添加一行：rospy  
  
然后运行  
roscore  
roslaunch tur...gazebo turtlebot3_world.launch  
rosrun tur...gazebo go.py  
（每个一个终端）  
  
launch: tur...simulation/tur..gazebo/launch  
world: tur...sim/tur...gaze/world  
sdf: tur...sim/tur..gaze/models/tur...burger  
urdf: turtlebot3/tur..description/urdf  
