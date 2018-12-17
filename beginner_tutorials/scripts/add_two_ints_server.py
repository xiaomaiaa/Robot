#!/usr/bin/env python

NAME = 'add_two_ints_server'

# import the AddTwoInts service
from beginner_tutorials.srv import *
import rospy 

def add_two_ints(req):
    req1=req.A
    req2=req.B
    print("Returning [%s + %s = %s]" % (req1, req2, (req1 + req2)))
    sum = req1 + req2
    return AddTwoIntsResponse(sum)

def add_two_ints_server():
    rospy.init_node(NAME)
    s = rospy.Service('add_two_ints', AddTwoInts, add_two_ints)
    print("Ready to add Two Ints")
    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

