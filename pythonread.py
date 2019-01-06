import os
import sys 
import time
import serial

port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)

firebase = firebase.FirebaseApplication('https://smarthome-3c6b9.firebaseio.com/', None) #Initiate Firebase

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


    #Method to read from Arduino and post a temperature value to Firebase
    def update_firebase_outSideTemp():
        dataRead = arduino.readline()
        if data is not None:
            time.sleep(1)
            pieces = data.split("sensor= ")
            temperature = pieces
            print temperature
        else:
            print('Failed to get data from Arduino.')
            time.sleep(10)

            data = {"Outside temperature": dataRead}
            firebase.post('/sensor/outside', data) #Post to some table in Firebase
            
            update_firebase_outSideTemp()
            time.sleep(5)        




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
