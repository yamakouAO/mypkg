# SPDX-FileCopyrightText: 2025 yamakouAO
# SPDX-License-Identifier: BSD-3-Clause

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import launch_ros.actions

def generate_launch_description():

    hour = LaunchConfiguration('hour')
    minute = LaunchConfiguration('minute')
    second = LaunchConfiguration('second')

    timer = launch_ros.actions.Node(
        package='mypkg',      #パッケージの名前を指定
        executable='timer',  #実行するファイルの指定
        arguments=[hour, minute, second],
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )
    return launch.LaunchDescription([
        DeclareLaunchArgument('hour', default_value='0'),
        DeclareLaunchArgument('minute', default_value='1'),
        DeclareLaunchArgument('second', default_value='0'),
        timer,
        listener]) 
