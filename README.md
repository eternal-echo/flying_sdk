# flying squirrel robot sdk

## 安装

激活环境
```shell
.\venv\Scripts\activate
```

## 使用

查看设备管理器中USB-Enhanced-SERIAL CH9102设备的端口号。我的是COM9。因此在代码中修改端口号为COM9。
```python
    # 初始化 Board
    board = Board(device="COM9")
```

### 舵机

修改`position`变量的值，设置舵机的角度，范围为0-180度

运行舵机示例
```shell
python3 examples/servo_example.py
```

### IMU

运行IMU示例
```shell
python3 .\examples\imu_example.py
```