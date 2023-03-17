from mfrc522 import MFRC522
import utime
from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

reader = MFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=0)
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)


lcd.putstr("Bring TAG closer...")


while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            if card == 3050636775:
                lcd.clear()
                lcd.blink_cursor_on()
                lcd.backlight_on()
                lcd.putstr("Access granted!")
                sleep(1)
            else:
                lcd.clear()
                lcd.blink_cursor_on()
                lcd.putstr("Access denied!")
                for i in range(5):
                    lcd.backlight_on()
                    sleep(0.2)
                    lcd.backlight_off()
                    sleep(0.2)
                lcd.backlight_on()
                sleep(1)
utime.sleep_ms(500) 

