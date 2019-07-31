#!/usr/bin/env python

import rospy
import serial

from gps_module.msg import gps_data


def talker():
	talker_topic = rospy.Publisher('chatter', gps_data, queue_size = 20)
	rospy.init_node('talker', anonymous = True)
	rate = rospy.Rate(10)
	msg = gps_data()
	ser = serial.Serial("/dev/ttyUSB0", baudrate = 9600)

	while not rospy.is_shutdown():
		mystr = str(ser.readline())
		mylist = mystr.split(",")
		GGA = "$GPGGA"

		if mylist[0]== GGA:
			print(mylist[0],"latitude:",mylist[2],"longitude:",mylist[4],"altitude:",mylist[9])
			msg.latitude = mylist[2]
			msg.longitude = mylist[4]
			msg.altitude = mylist[9]

			talker_topic.publish(msg)

		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
