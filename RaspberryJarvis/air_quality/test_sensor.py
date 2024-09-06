import serial, time
import datetime
import numpy as np
import sqlite3


def create_db():
    """Create a database"""
    try:
        sqliteConnection = sqlite3.connect("sqlite3.db")
        sqlite_create_table_query = """CREATE TABLE air_quality_temp (
                            id INTEGER PRIMARY KEY, 
                            pm25 NOT NULL, 
                            pm10 NOT NULL,
                            CREATED DATETIME DEFAULT CURRENT_TIMESTAMP 
                                    );"""

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

def connect_to_db():
    try:
        conn = sqlite3.connect('sqlite3.db')
        return conn
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)


def run():
    ser = serial.Serial("/dev/ttyUSB0")
    x_mean = []

    # create to table
    create_db()

    # connect to db
    conn = connect_to_db()
    

    while True:
        data = []
        for _ in range(0, 10):
            datum = ser.read()
            data.append(datum)

        pmtwofive = int.from_bytes(b"".join(data[2:4]), byteorder="little") / 10
        pmten = int.from_bytes(b"".join(data[4:6]), byteorder="little") / 10
        unknown = int.from_bytes(b"".join(data[:2]), byteorder="little") / 10
        unknown2 = int.from_bytes(b"".join(data[6:8]), byteorder="little") / 10

        dts = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        aq = {"PM25": pmtwofive, "PM10": pmten, "CREATED": dts}
        # Insert into temp table
        cur = conn.cursor()
        cur.execute("INSERT INTO air_quality_temp (PM25,PM10,CREATED) VALUES (?,?,?)",(pmtwofive,pmten,dts))
        conn.commit()
        print(aq)

    print(cur.lastrowid)
    # Commit to db
    conn.commit()

if __name__ == "__main__":
    run()
