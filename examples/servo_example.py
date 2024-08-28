import sys
import os

# 获取项目的根目录
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 将项目根目录添加到 sys.path
sys.path.append(project_root)

from flying_sdk.flying_controller_sdk import Board
import time

def simple_pwm_servo_test():
    # 初始化 Board
    board = Board(device="COM9")
    
    # 开启接收线程
    board.enable_reception()
    
    # 控制舵机位置
    servo_id = 1  # 假设控制舵机 1
    position = 2500  # 设置舵机位置，范围为0-180度，通常1ms-2ms (500-2500)

    # 设定舵机位置并读取偏移与位置
    board.pwm_servo_set_position(0.5, [[servo_id, position]])
    board.pwm_servo_set_offset(servo_id, 0)  # 设置偏移为 0

    # 读取舵机偏移量
    offset = board.pwm_servo_read_offset(servo_id)
    print(f"Servo {servo_id} Offset: {offset}")
    
    # 读取舵机当前位置
    current_position = board.pwm_servo_read_position(servo_id)
    print(f"Servo {servo_id} Current Position: {current_position}")

if __name__ == "__main__":
    simple_pwm_servo_test()
