#!/usr/bin/env python

import cv2
from cv_bridge import CvBridge, CvBridgeError

import rospy
from sensor_msgs.msg import Image


class MonoToColor(object):

    def __init__(self):
        rospy.init_node('mono_to_color')

        mono_image_topic = rospy.get_param('~mono_image_topic')
        color_image_topic = rospy.get_param('~color_image_topic')
        self.__frame_id = rospy.get_param('~frame_id', None)

        self.__bridge = CvBridge()

        self.__color_image_pub = rospy.Publisher(color_image_topic,
                                                 Image,
                                                 queue_size=1)

        self.__mono_image_sub = rospy.Subscriber(mono_image_topic,
                                                 Image,
                                                 self.__image_callback,
                                                 queue_size=1)

        rospy.loginfo('Initialized %s successfully.', self.__class__.__name__)

    def __image_callback(self, mono_image_msg):
        try:
            mono_image = self.__bridge.imgmsg_to_cv2(
                mono_image_msg, 'passthrough')
            color_image = cv2.cvtColor(mono_image, cv2.COLOR_GRAY2RGB)
            color_image_msg = self.__bridge.cv2_to_imgmsg(color_image, 'rgb8')
            rospy.loginfo('Converted mono to color image.')
            color_image_msg.header = mono_image_msg.header
            if self.__frame_id:
                color_image_msg.header.frame_id = self.__frame_id
            self.__color_image_pub.publish(color_image_msg)
        except CvBridgeError as e:
            rospy.logerr(e)


if __name__ == '__main__':
    MonoToColor()
    rospy.spin()
