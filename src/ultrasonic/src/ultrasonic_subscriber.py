#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
import config

def callback(data):     
    group_num = data.data[0]
    print("Group {} | ".format(int(group_num)),end=" ")
    for i, distance in enumerate(data.data[1:]):
        if distance < 300:
            print("{}: {}   |".format(int(i),distance),end=" ")
    if(group_num == 1.0):
        print("\n")

def listener(): 
    data_subs = []
    rospy.init_node('data_subscriber', anonymous=True)
    for i in range(config.NUM_GROUPS):
        data_subs.append(rospy.Subscriber('ultrasonic_data_group_{}'.format(i), Float64MultiArray, callback))
        
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()