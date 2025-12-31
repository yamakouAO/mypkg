#!/bin/bash -xv
# SPDX=FileCopyright: 2025 yamakouAO 
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" !="" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

ng () {
	res=1
}

res=0

cat /tmp/mypkg.log |
grep 'Listen: 10' || ng "$LINENO"

test "${res}" = 0 && echo OK
exit $res
