#sudo apt-get install ipython python-opencv python-scipy python-numpy python-pygame python-setuptools python-pip
#sudo pip install https://github.com/sightmachine/SimpleCV/zipball/develop
#sudo pip install svgwrite

import base64
import time
from SimpleCV import Camera
import json

data=json.loads('{"value":104,"time":1516165}')


def checkistempincreased(temp):
    if(temp>100):
        return True;
    return False;

def get_image():
    cam = Camera()
    img = cam.getImage()
    img.save("fireimg.png")

    time.sleep(1)
    encoded = base64.b64encode(open("fireimg.png", "rb").read())
    return encoded

while 1:
    if(checkistempincreased(data["value"])):
        encimg=get_image()
        data["img"]=encimg
        print json.dumps(data)
    time.sleep(1)
