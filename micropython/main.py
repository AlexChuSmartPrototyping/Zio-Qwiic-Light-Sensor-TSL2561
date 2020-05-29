"""
Demo code for Qwiic Light Sensor TSL2561, tested on pyboard
Auther: Alex Chu
Website: www.smart-prototyping.com
Email: shop@smart-prototyping.com
Qwiic Light Sensor TSL2561 product link: https://www.smart-prototyping.com/Zio-Qwiic-Light-Sensor-TSL2561
Display product link: https://www.smart-prototyping.com/Zio-OLED-Display-0-91-in-128-32-Qwiic.html
Library: https://github.com/adafruit/micropython-adafruit-tsl2561
"""

from machine import Pin,I2C
import tsl2561
from ssd1306 import SSD1306_I2C

i2c = I2C(sda=Pin("Y10"), scl=Pin("Y9"))
oled = SSD1306_I2C(128, 32, i2c, addr=0x3c)

light = tsl2561.TSL2561(i2c=i2c,address=0x39)

pyb.delay(100)
light.active(True)
pyb.delay(500)

while True:
    value = round(light.read(),2)
    oled.fill(0)
    oled.text("luminosity is:", 0, 0)
    oled.text(str(value) + " lux", 0, 20)
    pyb.delay(10)
    oled.show()
    pyb.delay(100)
