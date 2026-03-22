import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.pub = self.create_publisher(Int32,'/distance',10)
        self.timer = self.create_timer(1.0,self.send_data)

    def send_data(self):
        msg = Int32()
        msg.data = random.randint(0,100)
        self.pub.publish(msg)
        print(f"Publishing this number: {msg.data}")

def main():
    rclpy.init()
    node = DistancePublisher()
    rclpy.spin(node)
    rclpy.shutdown()
