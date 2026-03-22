import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')
        self.sub = self.create_subscription(
            Int32,
            '/distance',
            self.callback,
            10
        )

    def callback(self,msg):
        print(f"Yo,i got the number: {msg.data}")

def main():
    rclpy.init()
    node = DistanceSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
