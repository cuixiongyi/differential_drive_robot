cmake_minimum_required(VERSION 2.8.3)
project(test_robot)

find_package(catkin REQUIRED COMPONENTS
  cmake_modules
  geometry_msgs
  std_msgs
)

include (FindPkgConfig)
if (PKG_CONFIG_FOUND)
  pkg_check_modules(XML libxml-2.0)
else()
  message(FATAL_ERROR "pkg-config is required; please install it")
endif()

find_package(Boost REQUIRED COMPONENTS thread)

find_package(TinyXML REQUIRED)

catkin_package(

  CATKIN_DEPENDS
    geometry_msgs
    std_msgs

)


# Install Gazebo launch files
install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
