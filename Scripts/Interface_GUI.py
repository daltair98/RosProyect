#!/usr/bin/env python

import Tkinter as tk
from Tkinter import *
import rospy
from interface.msg import gps_data
from std_msgs.msg import String
from Interface.msg import Ip
from PIL import Image, ImageTk

class App():
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("720x480")
        self.root.wm_title("Serial Communication") #Makes the title that will appear in the top left
        self.root.config(background = "#FFFFFF")
        self.background = tk.PhotoImage(file="/home/rodrigo/catkin_ws/src/Interface/images/background.png") #Cambiar por la ruta donde se encuentre la imagen
        self.back = tk.Label(image=self.background)
        self.back.place(x=0,y=0,relwidth=1,relheight=1)
        rospy.init_node('listener')
        self.subGPS = rospy.Subscriber("gps_data", gps_data, self.GPS_Downloading)
        self.subXbox = rospy.Subscriber("Xbox", String, self.Xbox_control)
        self.subUser = rospy.Subscriber("Ip", Ip, self.Ip_User_Slave)

        #UPLEFT rame and its contents
        self.upLeftFrame = Frame(self.root, width=300, height = 600, bg="#045D69")
        self.upLeftFrame.grid(row=0, column=0, padx=35, pady=68)

        Label(self.upLeftFrame, text="GPS Data",fg="black",bg="#045D69",font=("Arial")).grid(row=0, column=0, padx=0, pady=2)

        Latitude = Label(self.upLeftFrame, text="1. Latitude:", bg="#045D69", fg="black")
        Latitude.grid(row=1, column=0, padx=0, pady=2)

        Longitude = Label(self.upLeftFrame, text="2. Longitude:", bg="#045D69", fg="black")
        Longitude.grid(row=2, column=0, padx=0, pady=2)

        Altitude = Label(self.upLeftFrame, text="3. Altitude:", bg="#045D69", fg="black")
        Altitude.grid(row=3, column=0, padx=0, pady=2)

        #MIDDLE Frame and its contents
        self.middleFrame = Frame(self.root, width=180, height = 40, bg="#045D69")
        self.middleFrame.grid(row=0, column=1, padx=60, pady=0)

        #UPRIGHT Frame and its contents
        self.upRightFrame = Frame(self.root, width=300, height = 600, bg="#045D69")
        self.upRightFrame.grid(row=0, column=2, padx=20, pady=2)

        Label(self.upRightFrame, text="AHRS Data:",fg="black",bg="#045D69",font=("Arial")).grid(row=0, column=0, padx=10, pady=2)

        #DOWN LEFT Frame and its contents
        self.leftFrame = Frame(self.root, width=150, height = 100, bg="#045D69")
        self.leftFrame.grid(row=1, column=0, padx=45, pady=100)

        Label(self.leftFrame, text="Temperature:",fg="black",bg="#045D69",font=("Arial")).grid(row=0, column=0, padx=10, pady=2)

        #DOWN RIGHT Frame and its contents
        self.rightFrame = Frame(self.root, width=150, height = 100, bg="#045D69")
        self.rightFrame.grid(row=1, column=2, padx=60, pady=100)

        Label(self.rightFrame, text="Distance:",fg="black",bg="#045D69",font=("Arial")).grid(row=0, column=0, padx=10, pady=2)


        self.root.mainloop()


    def GPS_Downloading(self, data):
       Longitude = Label(self.upLeftFrame, text=data.longitude, bg="#045D69", fg="black")
       Longitude.grid(row=1, column=1,padx=0,pady=0)

       Latitude = Label(self.upLeftFrame, text=data.latitude, bg="#045D69", fg="black")
       Latitude.grid(row=2, column=1,padx=0,pady=0)

       Altitude = Label(self.upLeftFrame, text=data.altitude, bg="#045D69", fg="black")
       Altitude.grid(row=3, column=1,padx=0,pady=0)

       self.root.after(1000, self, self.GPS_Downloading)

    def Ip_User_Slave(self, data):
        Label(text=data.Ip,fg="black",bg="#68A6DB",font=("Arial",11)).place(x=280, y=4)

    def Xbox_control(self,data):
       if data.data=="aa":
            load = Image.open("/home/rodrigo/catkin_ws/src/Interface/images/up.png")
            load = load.resize((100,100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label( image=render)
            img.image = render
            img.place(x=310, y=190)

       elif data.data=="bb":
            load=Image.open("/home/rodrigo/catkin_ws/src/Interface/images/down.png")
            load = load.resize((100,100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label( image=render)
            img.image = render
            img.place(x=310, y=190)

       elif data.data=="cc":
            load=Image.open("/home/rodrigo/catkin_ws/src/Interface/images/left.png")
            load = load.resize((100,100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label( image=render)
            img.image = render
            img.place(x=310, y=190)

       elif data.data=="dd":
            load=Image.open("/home/rodrigo/catkin_ws/src/Interface/images/right.png")
            load = load.resize((100,100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label( image=render)
            img.image = render
            img.place(x=310, y=190)

       else:
            load=Image.open("/home/rodrigo/catkin_ws/src/Interface/images/stop.jpg")
            load = load.resize((100,100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label( image=render)
            img.image = render
            img.place(x=310, y=190)



#if __name__ == '__main__':
app = App()
