# GPIO2 pin14 低电平点亮
import time
from machine import Pin,PWM


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('2-2-601', 'aa12345678')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()