#!/usr/bin/env python
import rospy
from std_msgs.msg import Time

def callback(data):     
    time_elapsed = rospy.get_rostime() - data
    if time_elapsed > 1:
        print("[ERROR]: Ultrasonic Heartbeat is not detected! Something is wrong!") #TODO: add better functionality should prob throw some type of error.

def listener(): 
    rospy.init_node('ultrasonic_stethoscope', anonymous=True)

    rospy.Subscriber("ultrasonic_heartbeat", Time, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()