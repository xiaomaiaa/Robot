#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
 
cmd_vel_pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
rospy.init_node('gogogo')
twist=Twist()
twist.linear.x=0.5
rate=rospy.Rate(10)
 
while not rospy.is_shutdown():
    cmd_vel_pub.publish(twist)

    # print "light_change_time : %f" % (light_change_time.to_sec())
    # print "rospy.Time.now    : %f" % (rospy.Time.now().to_sec())

    rate.sleep()
