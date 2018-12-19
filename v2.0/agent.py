#!/usr/bin/env python

import rospy
import time
from math import pi
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan1(msg):
    global range1
    range1=msg.ranges[135:225]
    range1=[round(i,2) for i in range1]

def scan2(msg):
    global mid_index,dis_mid,dis_min,min_index
    range2=msg.ranges[135:225]
    range2=[round(i,2) for i in range2]
    dis_min=1000
    dis_mid=range2[mid_index]
    for i in range(len(range2)):
        if abs(range1[i]-range2[i])>0.01:
            if range2[i]<dis_min:
                dis_min=range2[i]
                min_index=i

rospy.init_node('agent')
cmd_vel_pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
scan1_sub=rospy.Subscriber('scan1',LaserScan,scan1)
scan2_sub=rospy.Subscriber('scan2',LaserScan,scan2)
range1,range2=[],[]
mid_index,dis_mid,dis_min,min_index=45,1,0,0

twist=Twist()
rate=rospy.Rate(10)
 
while not rospy.is_shutdown():
    print 'dis_mid: ',dis_mid
    print 'dis_min: ',dis_min
    print 'min_index ',min_index
    if dis_mid<0.08:
        print 'wo diao ni ma de zhuang le a '
        twist.linear.x=0
        cmd_vel_pub.publish(twist)
        time.sleep(2)
        continue
    else:
        twist.linear.x=-0.1
        print 'min, mid: ',min_index,mid_index
        if min_index>mid_index+5:
            print 'left'
            diff=min_index-mid_index-5
            if diff>5:
                diff=5
            diff=diff/5.0
            twist.angular.z=diff*pi/4
        elif min_index<mid_index-5:
            print 'right'
            diff=min_index-mid_index+5
            if diff<-5:
                diff=-5
            diff=diff/5.0
            twist.angular.z=diff*pi/4
        else:
            print 'mid'
            twist.angular.z=0
        print 
    cmd_vel_pub.publish(twist)
    rate.sleep()