#!/usr/bin/env python
import rospy
import serial
from sensor_msgs.msg import Joy
from std_msgs.msg import String

def callback(data):
    if data.buttons[0] == 1:
        rospy.loginfo("ocho")
        pub.publish("ocho")
    elif data.buttons[1] == 1:
        rospy.loginfo("Tecla B")
        pub.publish("ww")
    elif data.buttons[2] == 1:
        rospy.loginfo("Tecla X")
        pub.publish("qq")#$psoc3,b#
    elif data.buttons[3]==1:
        rospy.loginfo("Cuadrado")
        pub.publish("asdasd")#$psoc3,x#
    elif data.axes[0] >= 0.8:
        rospy.loginfo("derecha")
        pub.publish("cc")
    elif data.axes[0] <= -0.8:
        rospy.loginfo("izquierda")
        pub.publish("dd")#$psoc1,01,10,10,01#
    elif data.axes[1] >= 0.8:
        rospy.loginfo("arriba")
        pub.publish("aa")
    elif data.axes[1] <= -0.8:
        rospy.loginfo("abajo")
        pub.publish("bb")#$psoc1,01,01,01,01#
    elif data.axes[2] <= -0.8:
        rospy.loginfo("PWM decrease")
        pub.publish("--")#$Psoc2,-#
        #estandar = "psoc2,-#"
    elif data.axes[5] <= -0.8:
        rospy.loginfo("PWM increase")
        pub.publish("++")
    else:
        rospy.loginfo("detente")
        pub.publish("xx")#$psoc1,00,00,00,00


# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    global ser
    ser = serial.Serial("/dev/ttyACM5", baudrate = 115200)
    pub = rospy.Publisher('Xbox', String, queue_size = 20)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('control')
    rospy.spin()

if __name__ == '__main__':
    start()
