#!/bin/bash -xv
# SPDX=FileCopyright: 2025 yamakouAO 
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" !="" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 100 ros2 launch mypkg timer_listen.launch.py> /tmp/mypkg.log

ng () {
	echo ${1}行目が違うよ
	res=1
}

res=0

cat /tmp/mypkg.log |
grep 'Remaining time: 60' || ng "$LINENO"

cat /tmp/mypkg.log |
grep 'TIME OUT' || ng "$LINENO"

cat /tmp/mypkg.log |
grep 'Over time: -10' || ng "$LINENO"

test "${res}" = 0 && echo OK
exit $res
