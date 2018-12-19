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
.xacro: turtlebot3/tur..description/urdf  
  
一般要开三个终端：  
roscore  
roslaunch turtl....gazebo turtlebot3_test.launch(加载世界)  
rosrun tur...gazebo automove.py（运行py）  
  
命令行中  
rostopic list：显示所有的话题  
  
v2.0（麦）：我只修改了两个xacro文件和agent.py，之后就只运行agent，不再使用automove或go  
  
V4.0：三个终端  
roscore  
roslaunch tur...gazebo turtlebot3_junk_move.launch  
rosrun tur..gazebo agent.py
