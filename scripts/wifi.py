import sys
import uasyncio as asyncio
if sys.platform != "linux":
    from machine import Pin

def connect():
    if sys.platform != "linux":
        led = Pin(2, Pin.OUT)
        led.on()

    if sys.platform == "linux":
        return

    import network
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('--', '--')
        while not sta_if.isconnected():
            # await asyncio.sleep(0.5)
            pass

    print('network config:', sta_if.ifconfig())
    if sys.platform != "linux":
        led.off()