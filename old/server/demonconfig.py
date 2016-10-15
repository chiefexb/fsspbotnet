import sys, time
import logging
import sys
import time
from neteria.server import NeteriaServer
from neteria.tools import _Middleware
def inform(st):
 f=open('./log','w')
 write(st)
 f.close()
 #logging.error(st)
 #print st
 return

# Create a middleware object that will echo events. "event_execute" is
# executed for every legal event message.

class EchoMiddleware(_Middleware):
    def event_legal(self, cuuid, euuid, event_data):
        return True

    def event_execute(self, cuuid, euuid, event_data):
        print event_data
        inform (event_data)  

# Create a client instance.
#server = NeteriaServer(EchoMiddleware())
#server.listen()


class SigFunctionsCon:
    
    def __init__(self,ourdaemon):
        self.__ourdaemon = ourdaemon
    
    def SIGTERM(self):
        sys.stderr.write("BB!\n")
        sys.exit(0)
        return

class ReactFunctionCon:
    
    def __init__(self,ourdaemon):
        self.__ourdaemon = ourdaemon
    
    def start(self):
        #server.listen()
        self.__ourdaemon.start()
    
    def stop(self):
        self.__ourdaemon.stop()
        
    def restart(self):
        self.__ourdaemon.restart()
        
    def startserver(self):
        #print message
        #NeteriaServer(EchoMiddleware())
        #server.listen()
        self.__ourdaemon.start()
        
class StatCon:
    
    strHelp = "Autmation has be applied to distribution sistem feeder for a long time, aspecially as related to protection and the restoration of some parts of the feeder."
    logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',level = logging.DEBUG, filename = './server.log')
    
    def run(self):
        server = NeteriaServer(EchoMiddleware())
        server.listen() 
        while(True):
           time.sleep(1)
    
    pidFile = "/tmp/daemon-naprimer.pid"
    
    inputter = "/dev/null"
    
    outputter = "/home/git/demout"
    
    errorer = "/home/git/dem"
