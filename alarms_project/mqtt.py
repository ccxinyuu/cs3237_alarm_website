import paho.mqtt.client as mqtt
from django.conf import settings
from .models import AlarmTone


def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('alarm/alarmtone')
    client.subscribe('alarm/time')
    client.subscribe('alarm/touch')
    client.subscribe('alarm/quit')


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def get_alarm_tone_choice():
    tone_dict = {"Love Story": 0, "Flower Dance": 1, "River Flows in You": 2, "Little Star": 3}
    # tone_choice = AlarmTone.objects.last()
    return tone_dict["Love Story"]


class MQTT:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
        self.client.connect(
            host=settings.MQTT_SERVER,
            port=settings.MQTT_PORT,
            keepalive=settings.MQTT_KEEPALIVE
        )
        self.client.loop_start()

    def publish_to_time(self):
        self.client.publish('alarm/time', payload=1, qos=0)
    
    def publish_to_alarm_tone(self, alarmtone):
        tone_dict = {"Love Story": 0 , "Flower Dance": 1, "River Flows in You":2, "Little Star": 3}
        self.client.publish('alarm/alarmtone', payload=tone_dict[alarmtone],qos=0)
    
    def publish_to_sleep_mode(self):
        self.client.publish('alarm/quit', payload = 1,  qos=0)
    
    def publish_to_turn_off_alarm(self):
        self.client.publish('alarm/touch', payload = 1, qos=0)

client = MQTT()

'''
from .models import AlarmTone
import paho.mqtt.client as mqtt
from time import time

#Connection success callback
    
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('alarm/alarmtone')
    client.subscribe('alarm/time')
    client.subscribe('alarm/touch')

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
def get_alarmTone_choice():
    tone_dict = {"Love Story": 0 , "Flower Dance": 1, "River Flows in You":2, "Little Star": 3}
    tone_choice = AlarmTone.objects.last()
    return tone_dict[tone_choice]


# set up mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('broker.emqx.io', 1883, 60)
client.username_pw_set("cs3237", "public")


client.publish('alarm/alarmtone',payload=1111 ,qos=0)
'''


