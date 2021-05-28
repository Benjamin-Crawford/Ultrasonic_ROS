#!/usr/bin/env python
from ultrasonic.src.config import NUM_GROUPS, URM13_ADDRESSES
from urm13 import urm13
import config
import rospy
from std_msgs.msg import Float64MultiArray, Time
import time

def publisher():
    heart_pub = rospy.Publisher('ultrasonic_heartbeat', Time, queue_size=10)

    rate = rospy.Rate(14) # 14hz
    data_pubs = []
    sensors = []

    for i in range(NUM_GROUPS):
        sensors.append([])
        data_pubs.append(rospy.Publisher('ultrasonic_data_group_{}'.format(i), Float64MultiArray, queue_size=10))
        rospy.init_node('data_publisher_group_{}'.format(i), anonymous=True)
        for j in GROUP_MEMBERS[i]:
            sensors[i].append(urm13(URM13_ADDRESSES[j]))

    while not rospy.is_shutdown():
        for i in range(NUM_GROUPS):
            distances = [i] #first item in distances array is the group number
            for sensor in sensors[i]:
                sensor.trigger_measurement()
            time.sleep(WAIT_TIME)
            for sensor in sensors[i]:
                distances.append(sensor.get_distance())
            rospy.loginfo(distances)
            data_pubs[i].publish(distances)

        heart_pub.publish(rospy.get_rostime())
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
