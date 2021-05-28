#!/usr/bin/env python
import config
from urm13 import urm13
import config
import rospy
from std_msgs.msg import Float64MultiArray, Float32
import time

def publisher():
    heart_pub = rospy.Publisher('ultrasonic_heartbeat', Float32, queue_size=10)

    data_pubs = []
    sensors = []

    for i in range(config.NUM_GROUPS):
        sensors.append([])
        data_pubs.append(rospy.Publisher('ultrasonic_data_group_{}'.format(i), Float64MultiArray, queue_size=10))
        rospy.init_node('data_publisher_group_{}'.format(i), anonymous=True)
        for j in config.GROUP_MEMBERS[i]:
            sensors[i].append(urm13(config.URM13_ADDRESSES[j]))

    rate = rospy.Rate(10) # 14hz
    while not rospy.is_shutdown():
        for i in range(config.NUM_GROUPS):
            data_to_send = Float64MultiArray()
            distances = [i] #first item in distances array is the group number
            for sensor in sensors[i]:
                sensor.trigger_measurement()
            time.sleep(config.WAIT_TIME)
            for sensor in sensors[i]:
                distances.append(sensor.get_distance())
            # rospy.loginfo(distances)
            data_to_send.data = distances
            data_pubs[i].publish(data_to_send)
        print(time.time())
        heart_pub.publish(time.time())
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
