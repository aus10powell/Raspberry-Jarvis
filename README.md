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
    * **Count Cars**
    * **Count Pedestrians**

## App Structure
```code
|-- RaspberryJarvis
|   |-- app.py
|   |-- /vision
|   |   |-- /templates
|   |   |   |-- /vision
|   |   |   |   |--take_picture.html
|   |   |   |   |--display_picture.html
|   |   |--vision.py
|   |-- /templates
|   |   |--template.html
|   |-- wsgi.py
|   |-- README.md
|   |-- requirements.txt



```

## Resources
* **Flask blueprint structure template:** https://hackersandslackers.com/flask-blueprints/
* **Following tutorial:** https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
* **Creating a flask app with authentication** https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login