#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
import config

def callback(data):     
    group_num = data[0]
    for i, distance in enumerate(data):
        print("Group Number {}: {}: {}, ".format(group_num,i,distance),end=" ")
    print("")

def listener(): 
    data_subs = []
    
    for i in range(config.NUM_GROUPS):
        rospy.init_node('data_subscriber_group_{}'.format(i), anonymous=True)
        data_subs.append(rospy.Subscriber('ultrasonic_data_group_{}'.format(i), Float64MultiArray, callback))
        
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()