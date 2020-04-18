import sys
import time
import argparse
from datetime import datetime
from base import MiBand2
from constants import ALERT_TYPES
import pytoml
import json
import random
import os
import paho.mqtt.publish as publish

SNIPS_CONFIG_PATH = '/etc/snips.toml'
siteId = 'default'
mqttServer = '127.0.0.1'
mqttPort = 1883
mqttUsername = ""
mqttPassword = ""

def loadConfigs():
    global mqttServer, mqttPort, siteId, hotwordId

    if os.path.isfile(SNIPS_CONFIG_PATH):
        with open(SNIPS_CONFIG_PATH) as confFile:
            configs = pytoml.load(confFile)
            if 'mqtt' in configs['snips-common']:
                if ':' in configs['snips-common']['mqtt']:
                    mqttServer = configs['snips-common']['mqtt'].split(':')[0]
                    mqttPort = int(configs['snips-common']['mqtt'].split(':')[1])
                elif '@' in configs['snips-common']['mqtt']:
                    mqttServer = configs['snips-common']['mqtt'].split('@')[0]
                    mqttPort = int(configs['snips-common']['mqtt'].split('@')[1])
                    
            if 'mqtt_username' in configs['snips-common']:
                mqttUsername = configs['snips-common']['mqtt_username']

            if 'mqtt_password' in configs['snips-common']:
                mqttPassword = configs['snips-common']['mqtt_password']
                
            if 'bind' in configs['snips-audio-server']:
                if ':' in configs['snips-audio-server']['bind']:
                    siteId = configs['snips-audio-server']['bind'].split(':')[0]
                elif '@' in configs['snips-audio-server']['bind']:
                    siteId = configs['snips-audio-server']['bind'].split('@')[0]
            if 'hotword_id' in configs['snips-hotword']:
                hotwordId = configs['snips-hotword']['hotword_id']
    else:
        print('Snips configs not found')


loadConfigs()
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--standard',  action='store_true',help='Shows device information')
parser.add_argument('-l', '--live',  action='store_true',help='Measures live heart rate')
parser.add_argument('-i', '--init',  action='store_true',help='Initializes the device')
parser.add_argument('-m', '--mac', default="EB:F0:3D:3E:4B:17", help='Mac address of the device')
args = parser.parse_args()

MAC = args.mac # sys.argv[1]
band = MiBand2(MAC, debug=True)
band.setSecurityLevel(level="medium")

if  args.init:
    if band.initialize():
        print("Init OK")
    band.set_heart_monitor_sleep_support(enabled=False)
    band.disconnect()
    sys.exit(0)
else:
    band.authenticate()

def buttonCallback():
    print("Button pressed")
    global mqttServer, mqttPort, siteId
    publish.single('hermes/hotword/default/detected', payload=json.dumps({
        'siteId': siteId,
        'modelId': "hey_snips",
        'modelVersion': "hey_snips_3.1_2018-04-13T15:27:35_model_0019",
        'modelType': "universal",
        'currentSensitivity': 0.5
    }), hostname=mqttServer, port=mqttPort, username=mqttUsername, password=mqttPassword)

if args.standard:
    print('### Standard Mode ###')
    print("Battery Level: " + str(band.get_battery_info()['level']))
    band.send_alert(ALERT_TYPES.MESSAGE)
    band.button_forever_listener(button_callback=buttonCallback)
    sys.exit()

def hearMesureCallback(val):
    print('Realtime heart:', val)

def heartRawCallback(val):
    print('Raw heart:', val)

def accelRawCallback(val):
    print('Raw accel heart:', val)

if args.live:
    print('### Live Mode ###')
    band.start_raw_data_realtime(
            heart_measure_callback=hearMesureCallback,
            heart_raw_callback=heartRawCallback,
            accel_raw_callback=accelRawCallback,
            button_callback=buttonCallback)

band.disconnect()
