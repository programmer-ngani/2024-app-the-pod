from machine import Pin
from time import sleep

limit_switch_top_l = Pin(6, Pin.IN, Pin.PULL_UP)
limit_switch_top_r = Pin(7, Pin.IN, Pin.PULL_UP)
limit_switch_btm_l = Pin(10, Pin.IN, Pin.PULL_UP)
limit_switch_btm_r = Pin(11, Pin.IN, Pin.PULL_UP)

print("test ready")

while True:
    while (limit_switch_top_l.value() == 1 and limit_switch_top_r.value() == 1):
        pass
    print("top reached")
    sleep(2)

while True:
    print("limit_switch_top_l", limit_switch_top_l.value())
    print("limit_switch_top_r", limit_switch_top_r.value())
    print("limit_switch_btm_l", limit_switch_btm_l.value())
    print("limit_switch_btm_r", limit_switch_btm_r.value())
    sleep(2)
    
