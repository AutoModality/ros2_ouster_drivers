#!/usr/bin/python3
# Copyright 2020, Steve Macenski
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os


def generate_launch_description():
    share_dir = get_package_share_directory('ros2_ouster')
    params_file = LaunchConfiguration('params_file')
    log_level = LaunchConfiguration('log_level')
    node_name = 'ouster_driver'

    # Acquire the driver param file
    params_file_launch_arg = DeclareLaunchArgument('params_file',
                                           default_value=os.path.join(
                                               share_dir, 'params', 'driver_config.yaml'),
                                           description='FPath to the ROS2 parameters file to use.')
    log_level_launch_arg = DeclareLaunchArgument('log_level', default_value='INFO')

    driver_node = Node(package='ros2_ouster',
                                executable='ouster_driver',
                                name=node_name,
                                output='screen',
                                emulate_tty=True,
                                parameters=[params_file],
                                arguments=['--ros-args', '--log-level', log_level],
                                namespace='/',
                                )


    return LaunchDescription([
        params_file_launch_arg,
        log_level_launch_arg,
        driver_node
    ])
