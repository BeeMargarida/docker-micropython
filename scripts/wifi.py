from machine import Pin
import uasyncio as asyncio

def connect():
    led = Pin(2, Pin.OUT)
    led.on()

    import network
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Calou oh puto do andar de cima', 'primodowilson')
        # sta_if.connect('raspberrypi', 'UJr2016#')
        while not sta_if.isconnected():
            # await asyncio.sleep(0.5)
            pass

    print('network config:', sta_if.ifconfig())
    led.off()