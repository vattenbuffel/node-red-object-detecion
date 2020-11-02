# Object detection using Node-red, yolo and raspberry pi
Take a photo with your phone, upload it and yolo will perform object detection on it and post the results to a Node-red dashboard.
The photo can also be an image which is stored locally on the computer.

# Instructions
<h2>Installation</h2>

Install [Node-red](https://nodered.org/#get-started) on a raspberry pi    
If you don't have a mqtt server you need one, [mosquitto](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/) works well  
Import the flows located in the directory flows
Install [yolo](https://medium.com/analytics-vidhya/raspberry-pi-tensorflow-2-installation-and-yolo-v3-object-detection-549f2346a3ab) on the desktop of the pi
Take the file "classify-node-red.py" and move it to the folder TensorFlow-2.x-YOLOv3

<h2>Usage</h2>
<h3>Photos which exist on a computer</h3>

Make sure the mqtt server and node-red are running  
Open localhost:1880/ui on a computer  
Switch to tab "Object detection" and upload an image  
The result should shown up after a short delay

<h3>Take photo with phone</h3>

Make sure the mqtt server and node-red are running  
Open localhost:1880/ui on a computer  
Switch to tab Phone object detection  
Open localhost:1880/camera on a phone/tablet  
Press upload file and take a photo  
The result should show up after a short delay


