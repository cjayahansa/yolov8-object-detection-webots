"""camera_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import cv2
import numpy as np


robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_wheel = robot.getDevice('left wheel motor')
right_wheel = robot.getDevice('right wheel motor')
left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
left_wheel.setVelocity(0.0)
right_wheel.setVelocity(0.0)


camera = robot.getDevice("camera")
camera.enable(timestep)

lower_red1 = np.array([0,120,70])
upper_red1 = np.array([10,255,255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])


while robot.step(timestep) != -1:

    img = camera.getImage()
    
    width = camera.getWidth()
    height = camera.getHeight()
    
    
    np_img = np.frombuffer(img, np.uint8).reshape((height, width, 4))
    frame = cv2.cvtColor(np_img, cv2.COLOR_BGRA2BGR)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1+mask2
    
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
        cv2.putText(frame, "Red", (x, y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2)
        
    cv2.imshow("WEBOTS+OPENCV:",frame)
    cv2.imshow("webots Camera",mask)
    cv2.waitKey(27)
    
   
    left_wheel.setVelocity(1.0)
    right_wheel.setVelocity(1.0)

