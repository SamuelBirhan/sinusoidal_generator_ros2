from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('sinusoidal_generator'),
        'config',
        'params.yaml'
    )

    return LaunchDescription([
        Node(
            package='sinusoidal_generator',
            executable='sin_generator',
            name='sin_generator',
            parameters=[config]
        ),
        Node(
            package='sinusoidal_generator',
            executable='scaler',
            name='scaler',
            parameters=[config]
        ),
        # Add rqt_plot to visualize the sine_wave and scaled_wave topics
        Node(
            package='rqt_plot',
            executable='rqt_plot',
            name='rqt_plot',
            arguments=['/sine_wave/data', '/scaled_wave/data']
        )
    ])
