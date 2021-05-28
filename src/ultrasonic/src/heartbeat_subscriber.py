#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Float32

def callback(data):     
    time_elapsed = time.time() - data.data
    if time_elapsed > 10:
        pass
        # print("[ERROR]: Ultrasonic Heartbeat is not detected! Something is wrong!") #TODO: add better functionality should prob throw some type of error.

def listener(): 
    rospy.init_node('ultrasonic_stethoscope', anonymous=True)

    rospy.Subscriber("ultrasonic_heartbeat", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()