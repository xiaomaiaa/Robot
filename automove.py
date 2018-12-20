#!/usr/bin/env python

import rospy
import time
from math import pi
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    global dis_ahead, mindis_index, mid_index,min_dis
    ranges=msg.ranges[90:270]
    dis_ahead=ranges[len(ranges)/2]
    mindis_index=ranges.index(min(ranges))
    min_dis=min(ranges)
    mid_index=len(ranges)/2

cmd_vel_pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
scan_sub=rospy.Subscriber('scan',LaserScan,scan_callback)
rospy.init_node('automove')
twist=Twist()
dis_ahead=1
min_dis=1
mindis_index=1
mid_index=1
rate=rospy.Rate(10)
 
while not rospy.is_shutdown():
    print 'dis ahead:%.2f'%dis_ahead
    if dis_ahead<0.2:
        twist.linear.x=0
        twist.angular.z=3*pi/4
        cmd_vel_pub.publish(twist)
        time.sleep(2) 
        continue
    else:
        twist.linear.x=-0.05
        if mindis_index>mid_index+10:
            twist.angular.z=pi/4
        elif mindis_index<mid_index-10:
            twist.angular.z=-pi/4
        else:
            twist.angular.z=0
    cmd_vel_pub.publish(twist)
    rate.sleep()
