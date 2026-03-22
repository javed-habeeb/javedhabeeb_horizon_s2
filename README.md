#  ROS2 publisher->subscriber task
this project completes the third objective that was shown in the 
document.this is the ros2 module that ustilises the publish and 
subscribe method to send and recieve messages between two nodes
'publish' and 'subscribe' using the '/distance' topic channel.

## how to use it
```
git clone <repo_url>
source install/setup.bash
```
either use two instances or by using tmux,type in each one
seperately like this

in 1st instance:
```
ros2 run distance_pkg publisher
```
in 2nd instance:
```
ros2 run distance_pkg subscriber
```
