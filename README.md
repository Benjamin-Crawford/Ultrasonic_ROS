# Ultrasonic_ROS
This project was created as a part of UCSD's ECE 191 Group Project class for the Triton AI club. It is intended to provide a ROS interface to the URM13 ultrasonic sensor in order to cover short range blindspots for autonomous vehicles. 

## Sensors:
We are using the URM13 ultrasonic sensors you can find more info about them on the store page here: https://www.dfrobot.com/product-2161.html  

## Requirements
We have tested this project on a Raspberry Pi running Ubuntu 20.04 and ROS Noetic. This project depends on the python libraries numpy and smbus2.  
ROS distro: http://wiki.ros.org/noetic/Installation   
numpy: ```pip install numpy```  
smbus2: ```pip install smbus2```  

## Installation
We have provided in this github repo the entire catkin workspace in order to ease installation into new ROS setups and cover any installation files. Therfore you should be able to just clone it into wherever you want to run it from. However if you want just the package you can just copy the files in the src/ultrasonic folder. 

## Setup
Each sensor must be setup before it can be used with the package. First run setup.py in src/ultrasonic/src/ this will guide you through the setup process. Next the file named config.py must be edited to match the addresses that you set earlier. Other settings in the config file will determine the initial configuration of the sensors when you start the ROS package. This also where you will specify the different groups of sensors to fire together. All of this is explained in the comments of the file so it should be very obvious what does what.  

For reference here is the link to the sensor wiki which details the sensor settings: https://wiki.dfrobot.com/URM13_Ultrasonic_Sensor_SKU_SEN0352  

## Usage

To use the package there are a few simple steps:  
  1. ssh into the pi  
  2. run `roscore` command  
  3. ssh into the pi again in another window  
  4. run `sudo -s` this is key because we need sudo privelages in order to run the package  
  5. navigate to the catkin_ws which will be the folder you cloned this repo into  
  6. run `source devel/setup.bash`   
  7. run `catkin_make`  
  8. navigate to the ultrasonic package located in src/ultrasonic  
  9. run `roslaunch ultrasonic ultrasonic.launch`  
 At this point the package should start running and if you are using the default subscriber provided you should start see readings from the sensors printing to the screen.  
 
 To add a new subscriber simply add the new .py file into the src/ultrasonic/src/ directory and then replace "subscriber.py" with its name in ultrasonic.launch  
 
 ## Using this package in a non-ROS context
 The file urm13.py contains a single class that describes all of the functionality of the URM13 sensor and easy access to its settings and could be useful for someone that wanted a simple way to interface with these sensors.   
