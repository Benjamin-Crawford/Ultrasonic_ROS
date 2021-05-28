#!/usr/bin/env python
from urm13 import urm13
import config
import rospy
from std_msgs.msg import Float64MultiArray, Bool

def publisher():
    data_pub = rospy.Publisher('ultrasonic_data', Float64MultiArray, queue_size=10)
    heart_pub = rospy.Publisher('ultrasonic_heartbeat', Bool, queue_size=10)
    rospy.init_node('data_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #TODO: add code to set up sensors
    while not rospy.is_shutdown():
        data = [] #TODO: add code to get actual data
        rospy.loginfo(data)
        data_pub.publish(data)
        heart_pub.publish(True)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
