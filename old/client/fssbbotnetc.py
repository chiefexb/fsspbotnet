#!/usr/bin/python

import logging
import sys
import time
from neteria.client import NeteriaClient
from neteria.tools import _Middleware
class EchoMiddleware(_Middleware):
    def event_legal(self, cuuid, euuid, event_data):
	return True
    def event_execute(self, cuuid, euuid, event_data):
	print event_data
	
# Create a client instance.
client = NeteriaClient()
client.listen()

# Discover a Neteria Server.
print "Discovering Neteria servers..."
while not client.registered:
    client.autodiscover()
    time.sleep(1)
print "Connected!"

# Send data to the server.
exit_cmds = ['quit', 'exit']
data = None
while data not in exit_cmds:
    data = str(raw_input("> "))
    if data:
        client.event(data)

sys.exit()

