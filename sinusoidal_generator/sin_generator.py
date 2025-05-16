#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class SinusoidalGenerator(Node):
    def __init__(self):
        super().__init__('sin_generator')
        self.publisher_ = self.create_publisher(Float32, 'sine_wave', 10)

        self.declare_parameter('amplitude', 1.0)
        self.declare_parameter('frequency', 1.0)

        self.amplitude = self.get_parameter('amplitude').value
        self.frequency = self.get_parameter('frequency').value

        self.timer = self.create_timer(self.time, self.publish_sine_wave)
        self.time = 0.0

    def publish_sine_wave(self):
        sine_value = self.amplitude * math.sin(2 * math.pi * self.frequency * self.time)
        msg = Float32()
        msg.data = sine_value
        self.publisher_.publish(msg)
        self.time += 0.1

def main(args=None):
    rclpy.init(args=args)
    node = SinusoidalGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
