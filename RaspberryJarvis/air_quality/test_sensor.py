import serial, time
import datetime
import numpy as np


def run():
    ser = serial.Serial("/dev/ttyUSB0")
    x_mean = []
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
        aq = {"PM25": pmtwofive, "PM10": pmten, "DTS": dts}
        print(aq)
        # x_mean.append(pmtwofive)
        # last_sixty = x_mean[-60:]
        # last_hour = x_mean[-3600:]
        # print(
        #     "pm25: {pmtwofive} pm10: {pmten} 1minMA: {minMA:.2f} 1minSTD: {minSTD:.2f} 1hrMA: {hrMA:.2f}".format(
        #         pmtwofive=pmtwofive,
        #         pmten=pmten,
        #         minMA=np.mean(last_sixty),
        #         minSTD=np.std(last_sixty),
        #         hrMA=np.mean(last_hour),
        #     )
        # )
        # print(aq," 1 min MA: ",np.mean(last_sixty), " 1min std:",np.std(last_sixty), " 1hr MA:",np.mean(last_hour))


if __name__ == "__main__":
    run()
