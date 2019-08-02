#!/usr/bin/env python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = socket.gethostname()   
s.connect(("8.8.8.8", 80))
#print(s.getsockname()[0])
us = hostname.split("-")
print("user: " + us[0] + "@" +s.getsockname()[0])    

s.close()
