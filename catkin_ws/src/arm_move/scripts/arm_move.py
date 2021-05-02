#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import math

def talker():
    pub1 = rospy.Publisher('/arm/joint3_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/arm/joint1_position_controller/command', Float64, queue_size=10)
    pub3 =  rospy.Publisher('/arm/joint2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    msg = Float64()
    x= float(input("input x:"))
    y= float(input("input y:"))
    z= float(input("input z:"))
    # Calculating theta1
    if (x)!=0:
        theta1=math.atan(y/x) + (math.pi/2)
    else:
        theta1=math.pi/2 + (math.pi/2)
    msg.data= theta1
    rospy.loginfo(msg)
    pub1.publish(msg)
    rate.sleep()
    pub1.publish(msg)
    rate.sleep()
    pub1.publish(msg)
    rate.sleep()
    # Calculating theta2
    
    hypo1=math.sqrt((x**2)+(y**2)) 
    left= z - 0.7
    phi2=math.atan(left/hypo1)+(38*math.pi/100)
    hypo2=math.sqrt((hypo1**2)+(left**2))
    num1=(((2.4)**2)-(3**2)-(hypo2**2))
    deno1=(-1*2*hypo2*3)
    print(num1/deno1)
    phi=math.acos(num1/deno1)
    theta2=phi-phi2
    msg.data= theta2 + (math.pi/2)
    num2=(((hypo2)**2)-(3**2)-((2.4)**2))
    deno2=(-1*2*2.4*3)
    phi3=math.acos(num2/deno2)
    theta3=((math.pi))-phi3
    msg.data= theta3 
    rospy.loginfo(msg)
    pub3.publish(msg)
    rate.sleep()
    pub3.publish(msg)
    rate.sleep()
    pub3.publish(msg)
    msg.data= theta2 + (math.pi/2)#-1.23
    rospy.loginfo(msg)
    pub2.publish(msg)
    rate.sleep()
    pub2.publish(msg)
    rate.sleep()
    pub2.publish(msg)
    rate.sleep()
    
    
if __name__ == "__main__":
    
     try:
        talker()
     except rospy.ROSInterruptException:
        pass