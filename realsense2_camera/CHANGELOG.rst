^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package realsense2_camera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Merge pull request `#27 <https://github.com/MisoRobotics/realsense/issues/27>`_ from MisoRobotics/user/ash/fix/emitter-issue
  Change default setting for RealSense emitters
* Change default setting for RealSense emitters
  The IR emitters for a RealSense camera was set to off by default.
  For some reason, this default setting was not working, and in order
  to turn the emitters off we had to toggle the emitters twice. By
  keeping them on by default, we can turn them off with only one toggle
  which is done in `chippy.rosinstall` for Frybot. The Grillbot needs
  them to be on.
* Merge pull request `#25 <https://github.com/MisoRobotics/realsense/issues/25>`_ from MisoRobotics/master
  Merge master back into develop
* Contributors: Nikita Kosolobov, Shreyash Gotee, Zach Zweig Vinegar

10.0.5 (2019-04-29)
-------------------
* Merge pull request `#22 <https://github.com/MisoRobotics/realsense/issues/22>`_ from MisoRobotics/user/zzv/fix/convert-log
  Remove log message in gray to color conversion
* Remove log message in gray to color conversion
  This log really gives us no information and is filling the logs
  making it difficult to find more important information.
* Merge pull request `#21 <https://github.com/MisoRobotics/realsense/issues/21>`_ from MisoRobotics/release/10.0.4
  release/10.0.4
* Contributors: Nikita Kosolobov, Ryan Sinnet, Zach Z-V

10.0.4 (2018-10-19)
-------------------
* Merge pull request `#19 <https://github.com/MisoRobotics/realsense/issues/19>`_ from MisoRobotics/feature/disable-emitter
  Disable RealSense emitter by default
* Disable RealSense emitter by default
  The projected IR pattern is interfering with marker detection now that
  the markers are closer to the cameras.
* Merge pull request `#18 <https://github.com/MisoRobotics/realsense/issues/18>`_ from MisoRobotics/release/10.0.3
  Release/10.0.3
* Contributors: Ryan Sinnet, Zach Z-V

10.0.3 (2018-09-14)
-------------------
* Merge pull request `#16 <https://github.com/MisoRobotics/realsense/issues/16>`_ from MisoRobotics/feature/disable-static-tfs
  Disable static transform publishing
* Disable static transform publishing
  This commit disables publishing of static transforms.  These are now
  being published by the Miso calibration service.
* Merge pull request `#14 <https://github.com/MisoRobotics/realsense/issues/14>`_ from MisoRobotics/release/10.0.2
  Release/10.0.2
* Contributors: Ryan Sinnet

10.0.2 (2018-08-29)
-------------------
* Merge pull request `#13 <https://github.com/MisoRobotics/realsense/issues/13>`_ from MisoRobotics/feature/ir-marker
  Feature/ir marker
  Add toggle for IR and RGB pointcloud and change default params
* Contributors: Zach Z-V

10.0.1 (2018-08-02)
-------------------
* Merge pull request `#10 <https://github.com/MisoRobotics/realsense/issues/10>`_ from MisoRobotics/feature/reset-exception
  Hardware reset of realsense on exception
* Merge pull request `#8 <https://github.com/MisoRobotics/realsense/issues/8>`_ from MisoRobotics/release/10.0.0
  Release/10.0.0
* Contributors: Nikita Kosolobov, Ryan Sinnet, Zach Z-V

10.0.0 (2018-07-30)
-------------------
* Merge pull request `#5 <https://github.com/MisoRobotics/realsense/issues/5>`_ from MisoRobotics/fix/cmake-release
  Fixed realsense not building in Release mode
* Fixed realsense not building in Release mode
* Lowering color resolution to 720p.
* Added namespace as tf prefix.
* Updating package.xml for format 2 and adding missing dependencies. Adding roslaunch-check.
* Disabled librealsense2 dependency for shippable.
* FHD and HD pointclouds working.
* HD color image now published correctly as well.
* Solid AR marker localization using nan workaround for ar_track_alvar.
* FHD Pointcloud kindof working, may have invalid depth values?
* Trying to publish fhd img with hd camera_info.
* Getting weird fuzzy img.
* Resizing not working yet.
* Contributors: Nikita Kosolobov, Ryan Sinnet, Shreyash Gotee, Zach Z-V

2.0.3 (2018-03-29)
------------------
* Merge pull request `#352 <https://github.com/MisoRobotics/realsense/issues/352>`_ from ruvu/feature/diagnostics
  Feature/diagnostics
* Corrected diagnostics naming of aligned streams (comment @icarpis)
* correct pointer to expected frequency
* Revert "Use nodehandles from nodelet"
  This reverts commit 03b0114bdca04ac8752c760495981c349b7ae595.
* Use nodehandles from nodelet
* Some logging
* diagnostic updaters with frequency status for publishers
* Merge pull request `#351 <https://github.com/MisoRobotics/realsense/issues/351>`_ from icarpis/development
  Bump version
* Bump version
* Merge pull request `#350 <https://github.com/MisoRobotics/realsense/issues/350>`_ from icarpis/development
  Improve CPU utilization using rs_rgbd.launch
* Fixed SR300 depth scale issue
* Check for subscribers before publish aligned frames
* Merge pull request `#324 <https://github.com/MisoRobotics/realsense/issues/324>`_ from icarpis/development
  Renaming ROS package from realsense_ros_camera to realsense2_camera
* Fixed merge issue
* Renaming ROS package from realsense_ros_camera to realsense2_camera
* Contributors: Itay Carpis, Rein Appeldoorn, icarpis

2.0.2 (2018-01-31)
------------------

2.0.1 (2017-11-02)
------------------

2.0.0 (2017-09-17)
------------------
