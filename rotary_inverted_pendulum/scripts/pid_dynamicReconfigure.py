#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import tkinter as tk
from tkinter import *

  

class pid_cfg_node:

    def __init__(self):        
        rospy.init_node('pid_cfg_node', anonymous=True)   
        self.kp = 15
        self.ki = 3
        self.kd = 0

        self.kp_pub = rospy.Publisher("/kp", Float64, queue_size=10)
        self.ki_pub = rospy.Publisher("/ki", Float64, queue_size=10)
        self.kd_pub = rospy.Publisher("/kd", Float64, queue_size=10)

        tkinter_window = tk.Tk()
        tkinter_window.geometry("500x200") 

        
    
        # self.kp_scale = tk.Scale(tkinter_window, from_=0, to=20, orient='horizontal', resolution = 0.01, command=self.update_param) 
        self.kp_scale = tk.Scale(tkinter_window, from_=0, to=100, orient='horizontal', resolution = 1 ) 
        self.kp_scale.grid(row=1,column=2)
        self.kp_scale.set(self.kp) 

        self.b1_1 = tk.Button(tkinter_window, text='-', command=lambda: self.kp_scale.set(self.kp_scale.get()-1))
        self.b1_1.grid(row=1,column=1)
        self.b1_2 = tk.Button(tkinter_window, text='+', command=lambda: self.kp_scale.set(self.kp_scale.get()+1))
        self.b1_2.grid(row=1,column=3)

        # b1 = tk.Button(my_w, text='+', width=10,command=lambda: my_upd())
        # b1.grid(row=2,column=1)

        # self.ki_scale = tk.Scale(tkinter_window, from_=0, to=1, orient='horizontal', resolution =   0.001, command=self.update_param)
        self.ki_scale = tk.Scale(tkinter_window, from_=0, to=10, orient='horizontal', resolution =   1 )
        self.ki_scale.grid(row=3,column=2)
        self.ki_scale.set(self.ki) 

        self.b2_1 = tk.Button(tkinter_window, text='-', command=lambda: self.ki_scale.set(self.ki_scale.get()-1))
        self.b2_1.grid(row=3,column=1)
        self.b2_2 = tk.Button(tkinter_window, text='+', command=lambda: self.ki_scale.set(self.ki_scale.get()+1))
        self.b2_2.grid(row=3,column=3)

        # self.kd_scale = tk.Scale(tkinter_window, from_=0, to=20, orient='horizontal', resolution =   0.01, command=self.update_param)
        self.kd_scale = tk.Scale(tkinter_window, from_=0, to=100, orient='horizontal', resolution =   0.1 )
        self.kd_scale.grid(row=5,column=2)
        self.kd_scale.set(self.kd) 

        self.b3_1 = tk.Button(tkinter_window, text='-', command=lambda: self.kd_scale.set(self.kd_scale.get()-0.1))
        self.b3_1.grid(row=5,column=1)
        self.b3_2 = tk.Button(tkinter_window, text='+', command=lambda: self.kd_scale.set(self.kd_scale.get()+0.1))
        self.b3_2.grid(row=5,column=3)

        self.b4_1 = tk.Button(tkinter_window, text='Update', command=self.update_param)
        self.b4_1.grid(row=6,column=1)

        self.b4_2 = tk.Button(tkinter_window, text='Reset', command=self.reset_param)
        self.b4_2.grid(row=6,column=3)


        self.update_param()


        tkinter_window.mainloop()

    def update_param(self, value=0):
            self.kp_pub.publish(self.kp_scale.get())
            self.ki_pub.publish(self.ki_scale.get())
            self.kd_pub.publish(self.kd_scale.get())

    def reset_param(self, value=0):
            self.kp_pub.publish(0)
            self.ki_pub.publish(0)
            self.kd_pub.publish(0)
    

  
if __name__ == '__main__':
      
    # you could name this function
    try:
        node = pid_cfg_node()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass