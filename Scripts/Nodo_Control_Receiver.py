#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    ser.write(data.data)
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("Xbox", String, callback)
    global ser
    ser = serial.Serial("/dev/ttyACM5", baudrate = 115200)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
