# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time
import random

from random import uniform

def get_Brightness(hour):
    if hour < 7:
        Brightness = 0
    elif hour < 10:
        Brightness = 1
    elif hour < 18:
        Brightness = 2
    elif hour < 21:
        Brightness = 1
    else:
        Brightness = 0
    return Brightness
          
def get_Presence():
    for i in range(3):
        if (random.random() > 0.5) == True: 
            Presence[i] = True
        else:
            Presence[i] = False
    return Presence


def get_Current_Status(Presence,Brightness):
    Current_Status = [False, False, False]
    for i in range(3):
        if (Brightness < 1): 
            Current_Status[i] = True

        elif ((Brightness < 2) and Presence[i]): 
            Current_Status[i] = True

        elif ((Brightness < 2) and not Presence[i]): 
            Current_Status[i] = False

        elif (Brightness == 2): 
            Current_Status[i] = False
    return Current_Status


def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))

def on_publish(client,userdata,mid):
    print("publish finished")
    pass

Brightness = 0 #de 0 a 2
Presence =  [False, False, False] 
Status = [False, False, False]

topic_Bri = ["/1234/Smartlight2017001/attrs/",
             "/1234/Smartlight2017002/attrs/",
             "/1234/Smartlight2017003/attrs/"]

topic_Pres =[ "/1234/Smartlight2017001/attrs/",
              "/1234/Smartlight2017002/attrs/",
              "/1234/Smartlight2017003/attrs/"]

topic_Stat = [ "/1234/Smartlight2017001/attrs/",
               "/1234/Smartlight2017002/attrs/",
               "/1234/Smartlight2017003/attrs/"]

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_publish

host = "130.206.112.29"
client.connect(host, port = 1883, keepalive = 60)
time.sleep(1)
client.loop_start()

hour = 0
while hour < 24:
    Brightness = get_Brightness(hour)
    Presence = get_Presence()
    Status = get_Current_Status(Presence,Brightness)
    
    for i in range(3):
        client.publish(topic_Bri[i], "bri:" + str(Brightness))
        client.publish(topic_Pres[i], "pres:" + str(Presence[i]))
        client.publish(topic_Stat[i], "sta:" + str(Status[i]))

    print("Hour " + str(hour))
    for i in range(3):
        print("SML" + str(i+1) + "  Lum: " + str(Brightness) +  "  Pres: " + str(Presence[i])  +  "  State: " + str(Status[i]))
    print("--------------------------------------------")
     
    time.sleep(2)
    hour += 1 #aumentamos de uno en uno la hora
    if hour == 24:
        hour = 0

