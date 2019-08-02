#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String

serial_port = serial.Serial("/dev/ttyUSB0", baudrate = 9600)
def AHRS():
    talker_estandar = rospy.Publisher('AHRS', String, queue_size = 20)
    rospy.init_node('AHRS', anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        string = str(serial_port.readline())
        talker_estandar.publish(string)
        print string

if __name__ == '__main__':
    try:
        AHRS()
    except rospy.ROSInterruptException:
        pass