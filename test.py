from pyitachip2sl import ITachIP2SLSocketClient
from time import sleep

hostname = '172.31.10.103'
port = 4999

itach = ITachIP2SLSocketClient(hostname, port)

#msg = itach.send_ascii_data('Status1')

#print(msg)

data = "\x08\x22\x00\x00\x00\x02\xD4"


on = itach.send_data('082200000002D4', True)

#off = itach.send_data('0x082200000001D5')

print(on)

