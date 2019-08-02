#!/usr/bin/env python

import rospy
import socket
from Interface.msg import Ip

def start():
    ip_publish = rospy.Publisher('Ip',Ip, queue_size = 20)
    rospy.init_node('Ip', anonymous = True)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = socket.gethostname()
    s.connect(("8.8.8.8", 80))
    us = hostname.split("-")
    prueba = "user: %s@%s"%(us[0],s.getsockname()[0])
    print(prueba)
    s.close()
    ip_publish.publish(prueba)

if __name__ == '__main__':
	try:
		start()
	except rospy.ROSInterruptException:
		pass
