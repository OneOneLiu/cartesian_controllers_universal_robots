#!/usr/bin/env python
import rospy
from geometry_msgs.msg import WrenchStamped

class WrenchFilter:
    def __init__(self):
        self.sub = rospy.Subscriber("wrench", WrenchStamped, self.callback)
        self.pub = rospy.Publisher("filtered_wrench", WrenchStamped, queue_size=10)
        self.tare_force = None
        self.tare_torque = None
        self.threshold = 30.0  # Define your threshold here

    def callback(self, msg):
        if self.tare_force is None:
            # Assume the first few seconds are used for taring
            self.tare_force = msg.wrench.force
            self.tare_torque = msg.wrench.torque
        else:
            # Apply tare and threshold
            force = msg.wrench.force
            torque = msg.wrench.torque
            force.x -= self.tare_force.x
            force.y -= self.tare_force.y
            force.z -= self.tare_force.z
            torque.x -= self.tare_torque.x
            torque.y -= self.tare_torque.y
            torque.z -= self.tare_torque.z
            
            # Apply threshold
            if abs(force.x) < self.threshold: force.x = 0
            if abs(force.y) < self.threshold: force.y = 0
            if abs(force.z) < self.threshold: force.z = 0
            if abs(torque.x) < self.threshold: torque.x = 0
            if abs(torque.y) < self.threshold: torque.y = 0
            if abs(torque.z) < self.threshold: torque.z = 0

            # Publish filtered data
            msg.wrench.force = force
            msg.wrench.torque = torque
            self.pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('wrench_filter')
    wf = WrenchFilter()
    rospy.spin()
