#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Scaler(Node):
    def __init__(self):
        super().__init__('scaler')
        self.subscription = self.create_subscription(Float32, 'sine_wave', self.scale_callback, 10)
        self.publisher_ = self.create_publisher(Float32, 'scaled_wave', 10)

        self.declare_parameter('scale', 1.0)
        self.scale = self.get_parameter('scale').value

    def scale_callback(self, msg):
        scaled_value = msg.data * self.scale
        scaled_msg = Float32()
        scaled_msg.data = scaled_value
        self.publisher_.publish(scaled_msg)

def main(args=None):
    rclpy.init(args=args)
    node = Scaler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
