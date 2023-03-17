from mfrc522 import MFRC522
import utime

reader = MFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=0)

print("Bring TAG closer...")
print("")


while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
utime.sleep_ms(500) 
