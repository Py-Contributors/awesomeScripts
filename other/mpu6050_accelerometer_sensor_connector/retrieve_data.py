import board
import busio
import adafruit_mpu6050
from mysql_connect import StoreToDatabase


if __name__ == "__main__":
    i2c = busio.I2C(board.SCL, board.SDA)
    mpu = adafruit_mpu6050.MPU6050(i2c)
    print("Current Temperature is: %.2f C" % mpu.temperature)
    while True:
        """Accelerometer Parameters"""
        acc_x = "%.4f" % mpu.acceleration[0]
        acc_y = "%.4f" % mpu.acceleration[1]
        acc_z = "%.4f" % mpu.acceleration[2]

        """Gyroscope Parameter"""
        gyro_x = "%.4f" % mpu.gyro[0]
        gyro_y = "%.4f" % mpu.gyro[1]
        gyro_z = "%.4f" % mpu.gyro[2]

        # DataCallibration.callibrate(acc_x, acc_y, acc_z)
        """Store sensor data to respective database"""
        StoreToDatabase.accelerometer_store(acc_x, acc_y, acc_z)
        StoreToDatabase.gyroscope_store(gyro_x, gyro_y, gyro_z)
