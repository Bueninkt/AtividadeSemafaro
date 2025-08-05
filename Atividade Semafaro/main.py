from machine import Pin
from utime import sleep

print("Hello World")

Verde = Pin(14, Pin.OUT)
Amarelo = Pin(12, Pin.OUT)
Vermelho = Pin(13, Pin.OUT)

while True:
    Verde.on()
    print("Verde Ligado")
    sleep(20)
    Verde.off()
    sleep(0.5)

    Amarelo.on()
    print("Amarelo Ligado")
    sleep(10)
    Amarelo.off()
    sleep(0.5)

    Vermelho.on()
    print("Vermelho Ligado")
    sleep(7)
    Vermelho.off()

