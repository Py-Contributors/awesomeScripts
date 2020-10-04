import mysql.connector
from mysql.connector import Error
import random

sid = random.randint(1, 100)


class StoreToDatabase:
    def check_if_connected():
        conn = None
        try:
            conn = mysql.connector.connect(
                host="192.168.100.7",
                database="dbname",
                user="uname",
                password="pass",
            )
            if conn.is_connected():
                return conn
        except Error as e:
            print(e)

    def accelerometer_store(acc_x, acc_y, acc_z):
        try:
            print(
                "Accelerometer Data:", sid, acc_x, acc_y, acc_z,
            )
            conn = StoreToDatabase.check_if_connected()
            insert_query = """INSERT INTO web_acmeter(sid, acc_x, acc_y, acc_z)
                                VALUES(%s, %s, %s, %s)"""
            cursor = conn.cursor()
            cursor.execute(insert_query, (sid, acc_x, acc_y, acc_z,))
            conn.commit()
        except Error as e:
            print(e)

    def gyroscope_store(gyro_x, gyro_y, gyro_z):
        try:
            conn = StoreToDatabase.check_if_connected()
            print("Gyroscope Data: ", sid, gyro_x, gyro_y, gyro_z)
            insert_query = """INSERT INTO web_gyro(sid, gyro_x, gyro_y, gyro_z)
                                    VALUES(%s, %s, %s, %s)"""
            cursor = conn.cursor()
            cursor.execute(insert_query, (sid, gyro_x, gyro_y, gyro_z))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
