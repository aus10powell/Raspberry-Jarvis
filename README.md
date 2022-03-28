# Raspberry Jarvis

************************************************************

## Current Capabilities:
* **Visual**
    * **View Images**
    * **Take pictures**

## Planned Capabilities:
* **Air Quality**
    * **PM2.5** Store data
    * **Inside Air Temp**
* **Visual**
    * **Show a streaming video**
    * **Count Cars**
    * **Count Pedestrians**
* **Sound**
    * **Capture a sound clip**

## App Structure

### App Structure
#### Current

#### Planned
```code
/RaspberryJarvis
├── /RaspberryJarvis
│   ├── __init__.py
│   ├── assets.py
│   ├── api.py
│   ├── /home
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /vision
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /air_quality
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /static
│   └── /templates
├── README.md
├── config.py
├── requirements.txt
└── wsgi.py
```

## Project Resources
* **Sound** 
    * *Noise-o-metter dashboard* https://github.com/yurivm/noise-o-meter
    * *Vehicle Sound Classification Using Deep Learning:*  https://webcache.googleusercontent.com/search?q=cache:XVV_BzYA6QEJ:https://www.analyticsvidhya.com/blog/2022/01/vehicle-sound-classification-using-deep-learning/+&cd=2&hl=en&ct=clnk&gl=us
* **Flask blueprint structure template:** Chose divisional structure so landing page won't find itself loading irrelevant CSS (faster).
    * https://hackersandslackers.com/flask-blueprints/
* **Following tutorial:** https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
* **Creating a flask app with authentication** https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

## Project Parts
* **Raspberry Pi 4**
* **SDS011:** Measures PM10 and PM5 particles
* **Raspberry Pi Camera Module V2-8 Megapixel,1080p**
* **ReSpeaker 4-Mic**

## Educational Resources Used
* **Local:** include  host="0.0.0.0", debug=True, port=3000 and run *python wsgi.py*
* **On-server:**
* **Setting up development locally** (I used a mac to ssh in using VScode)
    * **Development Site Techstack**
        * Server:
            * [How to serve Flask Applications in WSGI](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04#creating-a-uwsgi-configuration-file)
        * Flask
        * Bokeh
        * **Other**
            * [Setting up static IP](https://thepihut.com/blogs/raspberry-pi-tutorials/16683276-how-to-setup-a-static-ip-address-on-your-raspberry-pi)
            * [Flask Blueprints Divisional vs Functional](http://exploreflask.com/en/latest/blueprints.html#step-1-divisional-or-functional)