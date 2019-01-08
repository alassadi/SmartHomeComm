import os
import sys 
import time
import threading
import random
import serial


port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)


print(arduino.readline())

class Watcher(object):
    running = True
    refresh_milliSecond = 0.010

    # Constructor
    def __init__(self, watch_file, *args, **kwargs):
        self._cached_stamp = 0
        self.filename = watch_file
        self.args = args
        self.kwargs = kwargs
       

    # Look for changes
    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp

           

            thread = threading.Thread(target=self.writeaAndRespond())
            thread.daemon = True
            
      
            thread.start()
        





   
    def writeaAndRespond(self):
        filepath = r'./test.txt'
        f = open(filepath, 'r')
        line = f.readline()
        print(line+" sent.")
        arduino.write(str.encode(line))
          
        dataRead = arduino.readline()
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://fir-test-7f5bd.firebaseio.com/', None) 
        result = firebase.patch('/ResponseFromArduino',{'Response':dataRead}) 
        print(result)

      

      




    # Keep watching in a loop
    def watch(self):
        while self.running:
            try:
                # Look for changes
                time.sleep(self.refresh_milliSecond)
                self.look()
            except KeyboardInterrupt:
                print('\nDone')
                break
            except FileNotFoundError:
                # Action on file not found
                pass
            except:
                print('Unhandled error: %s' % sys.exc_info()[0])


watch_file = r'./test.txt'

# watcher = Watcher(watch_file)  # simple
watcher = Watcher(watch_file)  # also call custom action function
watcher.watch()  # start the watch going
