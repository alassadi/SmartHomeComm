import os
import sys 
import time
import serial

port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)

#print(arduino.readline())

class Watcher(object):
    running = True
    refresh_milliSecond = 0.002

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

            filepath = r'./test.txt'

            # File has changed, so do something...
            f = open(filepath, 'r')
            line = f.readline()
            print(line+" sent.")
            arduino.write(str.encode(line))
            #Mofification of Jimmy's method, write all responses we get from arduino to firebase. Firebase then sends it to clients via FCM.
            #dataRead = arduino.readline()
            from firebase import firebase
            firebase = firebase.FirebaseApplication('linktosmarthouse', None) 
            result = firebase.patch('/categoryinfirebase',{'Response':#dataRead}) 
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
