#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/arm/joint3_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.25) # 10hz
    msg = Float64()
    msg.data= 2.0
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
        msg.data+=0.1
    #rospy.spin()
if __name__ == "__main__":
    
     try:
        talker()
     except rospy.ROSInterruptException:
        pass