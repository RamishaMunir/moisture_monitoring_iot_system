from pymata4 import pymata4
import time
import gui_consol as ui
# from influxdb_client import InfluxDBClient
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime, time


bucket = "soil_moisture_bucket"
token = "LxT0hwaESudoDWMGpNofXVxKUfIcP5y4EaUE7ilKuAMGdAglOa2w6PK1_ZR3IwWJjo57DMd4_oz1jo-Uo2Ozig=="
org = "Student"

# testing
query = 'from(bucket: "soil_moisture_bucket")\
|> range(start: -10m)\
|> filter(fn: (r) => r._measurement == "soil_level_measurement")\
|> filter(fn: (r) => r._field == "soil_level")\
|> filter(fn: (r) => r.soil == "sensor_data")'

def initiate_db_settings():
    # establish a connection
    client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

    # instantiate the WriteAPI and QueryAPI
    write_api = client.write_api()
    query_api = client.query_api()
    return write_api, query_api

def detect_moisture_level():
    write_api, query_api = initiate_db_settings()
    board = pymata4.Pymata4()

    analog_pin = 1
    digital_pin = 13
    flag = False

    board.set_pin_mode_analog_input(analog_pin)
    board.set_pin_mode_digital_output(digital_pin)
    event_change_timestamp = 0

    while True:
        previous_event_change_timestamp = event_change_timestamp
        value, event_change_timestamp = board.analog_read(analog_pin)
        time.sleep(1)
        print(value, event_change_timestamp)
        if previous_event_change_timestamp != event_change_timestamp:
            p = Point("soil_level_measurement").tag("soil", "sensor_data").field("soil_level", int(value))
            write_api.write(SYNCHRONOUS)
            write_api.write(bucket=bucket, org=org, record=p)
            if ((value >= 500) & (flag == False)):
                board.digital_write(13, 1)
                flag = True
                time.sleep(1)
            if ((value < 500) & (flag == True)):
                board.digital_write(13, 0)
                flag = False
                time.sleep(1)


if __name__ == '__main__':
    detect_moisture_level()

#run this in browser
#http://localhost:8086/signin?returnTo=/orgs/2ebad06a47ce50f1/dashboards/08968a07f7eb4000