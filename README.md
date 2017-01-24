There is the draft version ROS packages released by Perc-china.

###Libraries used:(version beta3_RC5_22_12_2016_ww52)

<br /\>    SLAM: libreansense_slam.so. 

<br /\>    PT: librealsense_persontracking.so. 

<br /\>    CAMERA: librealsense.so. 

The release notes in the packages are draft version, they will be updated very soon. Thanks.
 
## Installation Instructions

Assuming that ROS Kinetic has already been installed following the instructions at http://wiki.ros.org/kinetic/Installation/Ubuntu, the steps below can be used to compile these ROS nodes for RealSense:
```bash
$ sudo apt-key adv --keyserver keys.gnupg.net --recv-key AFF33D2C
$ echo 'deb "http://jenkinsperc01.iil.intel.com:8080/userContent/freight-release-staging" xenial main' | sudo tee /etc/apt/sources.list.d/perc-release-staging.list
$ sudo apt update
$ sudo apt install librealsense-all-dev
$ mkdir –p catkin_ws/src
$ cd catkin_ws/src
$ catkin_init_workspace
$ git clone http://github.com/IntelRealSense/realsense-ros
$ cd ..
$ catkin_make
$ source devel/setup.bash
$ roslaunch realsense-camera realsense-camera-demo
```

**Note**: These instructions above currently use a different librealsense than provided publically as part of the ROS build farm.  Do not install ros-kinetic-realsense-camera or ros-kinetic-librealsense, otherwise the steps above will not work correctly. 

## Additional Information
For additional information about this repository, see https://wiki.ith.intel.com/display/perceptual/Guidelines+for+RealSense+SDK+ROS+Samples
