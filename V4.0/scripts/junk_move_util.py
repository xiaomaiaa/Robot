#!/usr/bin/env python

import rospy
import time
from math import pi
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

dis_ahead=1
min_dis=1
mindis_index=1
mid_index=1


class jm(object):
    def __init__(self,junk_id):
        self.junk_id=junk_id
        pass
    
    def do(self):
        junk_id=self.junk_id
        junk_move_topic="tb3_"+str(junk_id)+"/cmd_vel"
        junk_scan_topic="tb3_"+str(junk_id)+"/scan"
       
        
        def scan_callback(msg):
            global dis_ahead,min_dis,mindis_index,mid_index
            ranges=msg.ranges[:]
            dis_ahead=ranges[len(ranges)//2]
            mindis_index=ranges.index(min(ranges))
            min_dis=min(ranges)
            mid_index=len(ranges)//2
            

        cmd_vel_pub=rospy.Publisher(junk_move_topic,Twist,queue_size=1)
        scan_sub=rospy.Subscriber(junk_scan_topic,LaserScan,scan_callback)
        rospy.init_node('junk0')
        twist=Twist()
        
        rate=rospy.Rate(10)
        flag=0#once beginning moving ,it will move for a long time
        move_cnt=0
        move_max_cnt=100


        while not rospy.is_shutdown():
            print('dis min:%.2f'%min_dis)
            

            if min_dis<0.4 or flag==1:
                time.sleep(3)
                twist.linear.x=-1000
                twist.angular.z=0
                cmd_vel_pub.publish(twist)
                flag=1
                move_cnt=move_cnt+1
                if move_cnt>move_max_cnt:
                    flag=0
                #time.sleep(2) 
                
                continue
            else:
                # twist.linear.x=-0.5
                # if mindis_index>mid_index+10:
                #     twist.angular.z=pi/4
                # elif mindis_index<mid_index-10:
                #     twist.angular.z=-pi/4
                # else:
                #     twist.angular.z=0
                twist.linear.x=0
                #time.sleep(2)
                pass
            cmd_vel_pub.publish(twist)
            rate.sleep()
