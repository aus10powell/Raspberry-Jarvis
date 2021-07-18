from flask import Blueprint, render_template, request, Markup
import json
from plotly import utils
import plotly.express as px
import pandas as pd
import serial, time
import numpy as np
import datetime
import logging

air_quality_bp = Blueprint(
    "air_quality_bp", __name__, static_folder="static", template_folder="templates"
)


def gm(country="United Kingdom"):
    from plotly import utils

    df = pd.DataFrame(px.data.gapminder())

    country = country.strip()
    fig = px.line(df[df["country"] == country], x="year", y="gdpPercap", title=f"{country}")
    if country not in df["country"].unique(): logging.warning("{} country not in dataset".format(country))
    print("Plotting country {}".format(country))
    graphJSON = json.dumps(fig, cls=utils.PlotlyJSONEncoder)
    return graphJSON


@air_quality_bp.route("/callback", methods=["POST", "GET"])
def cb():
    print("Received a request to plot country {}".format(request.args.get("data")))
    return gm(request.args.get("data"))


@air_quality_bp.route("/plotly", methods=["GET", "POST"])
def plotly():
    return render_template("chartsajax.html", graphJSON=gm())

@air_quality_bp.route("/start_sensor",methods=["GET"])
def start_sensor():
    loggin.info("Starting air quality data collection")
    ser = serial.Serial("/dev/ttyUSB0")

    x_mean = []
    while True:
        data = []
        for _ in range(0, 10):
            datum = ser.read()
            data.append(datum)

        pmtwofive = int.from_bytes(b"".join(data[2:4]), byteorder="little") / 10
        pmten = int.from_bytes(b"".join(data[4:6]), byteorder="little") / 10

        ts = time.time()
        dts = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        aq = {"PM25": pmtwofive, "PM10": pmten, "ts": dts}
        x_mean.append(pmtwofive)
        last_sixty = x_mean[-60:]
        last_hour = x_mean[-3600:]
        print(
            "pm25: {pmtwofive} pm10: {pmten} 1minMA: {minMA:.2f} 1minSTD: {minSTD:.2f} 1hrMA: {hrMA:.2f}".format(
                pmtwofive=pmtwofive,
                pmten=pmten,
                minMA=np.mean(last_sixty),
                minSTD=np.std(last_sixty),
                hrMA=np.mean(last_hour),
            )
        )



if __name__ == "__main__":
    air_quality_bp.run()
