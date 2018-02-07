from xbos import get_client
import msgpack
import time
import datetime, pytz

c = get_client()

'''
def on_msg(msg):
    for po in msg.payload_objects:
        if po.type_dotted == (2,9,9,9):
            data = msgpack.unpackb(po.content)
            print "DR EVENT", data
            prices = data
'''
'''
c.subscribe("xbos/events/dr/s.dr/sdb/i.xbos.dr_signal/signal/signal", on_msg)
print "Listening for DR events"
while True:
    time.sleep(30)
    print prices
'''


msg = c.query("xbos/events/dr/s.dr/sdb/i.xbos.dr_signal/signal/signal")[0]
#print msg

#now=datetime.datetime.utcnow().replace(tzinfo=pytz.timezone("UTC")).astimezone(tz=pytz.timezone("America/Los_Angeles"))
#temp_now = self.now + timedelta(minutes=time*period)


for po in msg.payload_objects:
	if po.type_dotted == (2,9,9,9):
		data = msgpack.unpackb(po.content)
print "DR EVENT", data




