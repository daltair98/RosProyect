# ALL THE SCRIPTS ARE BEING TESTED IN THE beginner_tutorials from ROS

From the code Node_GUI.py the import:

> self.background = tk.PhotoImage(file="/home/rodrigo/catkin_ws/src/beginner_tutorials/images/background.png")

It's to import a background for the interface, the direction it doesn't matter as long as the full link from your computer is written

At the end of the project all nodes will be connected, the sensors Node have to be in the raspberry pi, while the Control_node and the GUI_node have to be in your computer

## Naming the files
The standar to name an individual proyect per sensor must be
> [NameOfModule]_module
 
And the node python file
> Node_[NameOfModule]
 
The ROS master needs to have the same custom messages as the slave in order to subscribe and gather the information, the name has to be
> [NameOfModule]_data
