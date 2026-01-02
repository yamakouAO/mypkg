# SPDX-FileCopyrightText: 2025 yamakouAO
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import sys

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
time = int(sys.argv[1])*3600 + int(sys.argv[2])*60 + int(sys.argv[3])


def cb():
    global time
    msg = Int16()
    msg.data = time
    pub.publish(msg)
    time -= 1


def main(): 
    node.create_timer(1, cb)
    rclpy.spin(node)

