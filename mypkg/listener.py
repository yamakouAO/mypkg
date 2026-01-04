# SPDX-FileCopyrightText: 2025 yamakouAO
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
<<<<<<< HEAD
    node.get_logger().info("Listen: %s" % msg)

=======
    if msg.data > 0:
        node.get_logger().info("Remaining time: %d" % msg.data)
    elif msg.data == 0:
        node.get_logger().info("TIME OUT")
    else:
        node.get_logger().info("Over time: %d" % msg.data)
>>>>>>> dev

def main():
    pub = node.create_subscription(Person, "person", cb, 10)
    rclpy.spin(node)
