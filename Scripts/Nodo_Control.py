#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import String

def callback(data):
    if data.buttons[0] == 1:
        rospy.loginfo("ocho")
        pub.publish("ocho")
    elif data.buttons[1] == 1:
        rospy.loginfo("cuadrado")
        pub.publish("cuadrado")
    elif data.buttons[2] == 1:
        rospy.loginfo("gira sobre el eje derecha")
        pub.publish("gira sobre la derecha")
    elif data.buttons[3]==1:
        rospy.loginfo("gira sobre el eje izquierda")
        pub.publish("gira sobre la izquierda")
    elif data.axes[0] >= 0.8:
        rospy.loginfo("derecha")
        pub.publish("derecha")
    elif data.axes[0] <= -0.8:
        rospy.loginfo("izquierda")
        pub.publish("izquierda")
    elif data.axes[1] >= 0.8:
        rospy.loginfo("arriba")
        pub.publish("arriba")
    elif data.axes[1] <= -0.8:
        rospy.loginfo("abajo")
        pub.publish("abajo")
    elif data.axes[2] <= 0.8:
        rospy.loginfo("PWM decrease")
        pub.publish("-PWM")
    elif data.axes[5] <= 0.8:
        rospy.loginfo("PWM increase")
        pub.publish("+PWM")
    else:
        rospy.loginfo("detente")
        pub.publish("stop")

  


def start():
    global pub
    pub = rospy.Publisher('Xbox', String)
    rospy.Subscriber("joy", Joy, callback)
    rospy.init_node('control')
    rospy.spin()

if __name__ == '__main__':
    start()
