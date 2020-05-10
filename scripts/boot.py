# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
# import uos
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
#gc.collect()

##############################

import sys
import wifi
from server import Server

client_id = None
print(sys.argv)

if(len(sys.argv) > 1):
    client_id = sys.argv[1]

wifi.connect()
server = Server(client_id)
