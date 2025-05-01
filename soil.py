from pymata4 import pymata4
import time
from database import Database
import gui_consol as ui


def create_db():
    schema_name = "iot_application"
    db_conf = {'host': 'localhost', 'port': '3306', 'user': 'root', 'pasw': '123456'}
    rdb = Database(schema=schema_name, **db_conf)
    engine = rdb.create_engine()
    return engine

def detect_moisture_level():
    connection = create_db()

    board = pymata4.Pymata4()

    analog_pin = 1
    digital_pin = 13
    flag = False

    board.set_pin_mode_analog_input(analog_pin)
    # board.set_pin_mode_digital_input(digital_pin)
    board.set_pin_mode_digital_output(digital_pin)

    while True:
        value, timestamp = board.analog_read(analog_pin)
        print(value, timestamp)
        # ui.yn_lbl.config(text=value)
        time.sleep(1)
        connection.execute(f"insert into moisture_level_values (moisture_value) values ({value})")
        if ((value >= 1000) & (flag == False)):
            board.digital_write(13, 1)
            flag = True
            time.sleep(1)
        if ((value < 1000) & (flag == True)):
            board.digital_write(13, 0)
            flag = False
            time.sleep(1)


if __name__ == '__main__':
    detect_moisture_level()
    # ui.vp_start_gui()
