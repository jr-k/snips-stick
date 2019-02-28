import sys
import time
import argparse
from datetime import datetime
from base import MiBand2
from constants import ALERT_TYPES

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
    print("Hey")

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
            accel_raw_callback=accelRawCallback)

band.disconnect()
