# timerコマンド

![test](https://github.com/yamakouAO/mypkg/actions/workflows/test.yml/badge.svg)
### テスト環境
- Ubuntu 22.04 LTS
### 概要
ROS2を用いた、タイマーです。
* **timer**: 指定した時間からどれだけ時間が経っているかを計測。
* **listener**: 指定した時間までの残り時間を/countupからメッセージをもらって表示、指定した時間よりも超過した場合超過時間を表示。

## 使い方
### 実行方法
* ros2 runで1分タイマーを実行:入力は、０時間１分０秒
```
端末1$ ros2 run mypkg timer 0 1 0
端末2$ ros2 run mypkg listener
[INFO] [listener]: Remaining time: 60
[INFO] [listener]: Remaining time: 59
[INFO] [listener]: Remaining time: 58
...
[INFO] [listener]: Remaining time: 1
[INFO] [listener]: TIME OUT
[INFO] [listener]: Over time: -1
[INFO] [listener]: Over time: -2
```

* launchファイルを用いる場合:入力は、０時間１分30秒
```
$  ros2 launch mypkg timer_listen.launch.py hour:=0 minute:=1 second:=30
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [timer-1]: process started with pid [86606]
[INFO] [listener-2]: process started with pid [86608]
[listener-2] [INFO] [1767493473.109778034] [listener]: Remaining time: 90
[listener-2] [INFO] [1767493474.085137772] [listener]: Remaining time: 89
[listener-2] [INFO] [1767493475.084799649] [listener]: Remaining time: 88
...
[listener-2] [INFO] [1767493562.085222424] [listener]: Remaining time: 1
[listener-2] [INFO] [1767493563.085050553] [listener]: TIME OUT
[listener-2] [INFO] [1767493564.085082581] [listener]: Over time: -1
[listener-2] [INFO] [1767493565.085429157] [listener]: Over time: -2
[listener-2] [INFO] [1767493566.085092049] [listener]: Over time: -3
```

## 動作環境
- Ubuntu 22.04 LTS

## ライセンス
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
	- [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 yamakouAO

