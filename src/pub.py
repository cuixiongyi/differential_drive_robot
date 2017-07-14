import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
import rospy
import roslib; 
# roslib.load_manifest('gazebo')
from gazebo_msgs.srv import *

def gms_client(model_name,relative_entity_name):
    rospy.wait_for_service('/gazebo/get_model_state')
    try:
        gms = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp1 = gms(model_name,relative_entity_name)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def setObject():
    objName = 'test_robot'
    pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=10)
    rospy.init_node('setObject', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        msg = ModelState() 
        resp1 = gms_client(objName,objName)
        msg = ModelState() 
        msg.pose = resp1.pose
        msg.twist = resp1.twist
        msg.pose.position.x += .30 
        msg.model_name = objName
        print msg
        pub.publish(msg)
        rate.sleep()
        print  "here"

if __name__ == '__main__':
    try:
        setObject()
    except rospy.ROSInterruptException:
        pass
