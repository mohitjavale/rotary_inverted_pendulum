#!/usr/bin/env python

import math  
import rospy
from std_msgs.msg import String, Float64
from sensor_msgs.msg import JointState
  

class pid_plain_node:

    def __init__(self):        
        rospy.init_node('pid_plain_node', anonymous=True)         

        self.pendulum_set_point = 0
        self.pendulum_process_value = 0
        self.pendulum_last_process_value = 0
        self.kp = 15
        self.ki = 3
        self.kd = 0
        self.p = 0
        self.i = 0
        self.d = 0
        self.last_output = 0
        self.output = 0

        self.output_pub = rospy.Publisher("/rotary_inverted_pendulum/Rev1_position_controller/command", Float64, queue_size=10)
        self.angle_pub = rospy.Publisher("/angle", Float64, queue_size=10)
        # self.rate = rospy.Rate(50)
        self.input_sub = rospy.Subscriber("/rotary_inverted_pendulum/joint_states", JointState, self.joint_states_callback)
        

        self.kp_sub = rospy.Subscriber("/kp", Float64, self.kp_update)
        self.ki_sub = rospy.Subscriber("/ki", Float64, self.ki_update)
        self.kd_sub = rospy.Subscriber("/kd", Float64, self.kd_update)

        print('Subscription Estabilshed')

    def kp_update(self, data):
        self.kp = data.data
        print(f'new kp = {self.kp}')
        self.i = 0

    def ki_update(self, data):
        self.ki = data.data
        print(f'new ki = {self.ki}')
        self.i = 0

    def kd_update(self, data):
        self.kd = data.data
        print(f'new kd = {self.kd}')
        self.i = 0

    def joint_states_callback(self, data): 
        self.pendulum_last_process_value = self.pendulum_process_value
        self.pendulum_process_value = data.position[1]
        self.pendulum_process_value = self.pendulum_process_value % (2*math.pi)
        if self.pendulum_process_value > math.pi:
            self.pendulum_process_value = self.pendulum_process_value-(2*math.pi)
        self.angle_pub.publish(self.pendulum_process_value)
        self.p = self.pendulum_set_point - self.pendulum_process_value
        self.i += self.p
        self.d = self.pendulum_process_value-self.pendulum_last_process_value 
        self.last_output = self.output

        # if abs(self.pendulum_process_value) > 0.1:
        #     self.kp = 0
        #     self.ki = 0
        #     self.kd = 1.4
        self.output = (self.kp*self.p + self.ki*self.i + self.kd*self.d)
        self.output_pub.publish(self.output)
        print(f'p = {self.p} i = {self.i} d = {self.d}')
        # print(f"output = {self.output}")
    

  
if __name__ == '__main__':
      
    # you could name this function
    try:
        node = pid_plain_node()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass