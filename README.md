# pyitachip2sl
Python3 interface for sending serial commands via GlobalCache iTach IP to Serial device

## Notes
This was developed for use with [Home-Assistant](http://home-assistant.io) but is usable by any python application.

## Usage
```python
from pyitachip2sl import ITachIP2SLSocketClient

hostname = '10.0.0.50'
port = 4999 # Optional parameter, defaults to 4999
timeout = 1 # Optional parameter, defaults to 1

itach = ITachIP2SLSocketClient(hostname, port, timeout)

# Send ASCII command
itach.send_data("Status1.")

# Send ASCII command and retrieve response
response = itach.send_data("Status1.")
print(response)

# Send raw data
itach.send_data("082200000002D4", True)
```
