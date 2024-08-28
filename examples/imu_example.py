#!/usr/bin/env python3
# encoding: utf-8

import sys
import os

# 获取项目的根目录
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 将项目根目录添加到 sys.path
sys.path.append(project_root)

import csv
import time
import threading
from flying_sdk.flying_controller_sdk import Board  # Assuming the SDK is structured like this

def write_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def imu_data_collection(board, csv_filename):
    board.enable_reception()
    print("Collecting IMU data...")

    # Create the CSV file with headers
    write_to_csv(csv_filename, ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z"])

    while True:
        try:
            imu_data = board.get_imu()
            if imu_data is not None:
                # Get timestamp
                timestamp = time.time()

                # Log the IMU data to CSV
                imu_row = [timestamp] + list(imu_data)
                write_to_csv(csv_filename, imu_row)

                # Print the IMU data for reference
                print(f"IMU Data: {imu_row}")

            # Short sleep to avoid excessive CPU usage
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("Stopping data collection...")
            break

if __name__ == "__main__":
    # Initialize the board
    board = Board(device="COM9")

    # Define the output CSV file
    csv_filename = "./examples/output/imu_data.csv"

    # Start the data collection
    imu_data_collection(board, csv_filename)
