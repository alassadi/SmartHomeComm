import os
import sys 
import time
import serial
from firebase import firebase

port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)

firebase = firebase.FirebaseApplication('https://smarthome-3c6b9.firebaseio.com/', None) #Initiate Firebase

#print(arduino.readline())

class Watcher(object):
    running = True
    refresh_milliSecond = 0.010

    # Constructor
    def __init__(self, watch_file, *args, **kwargs):
        self._cached_stamp = 0
        self.filename = watch_file
        self.args = args
        self.kwargs = kwargs
        #thread = threading.Thread(target=self.checkFire, args=()) Background thread that is running occassionally to look if house is on fire.
        #thread.daemon = True
        #thread.start()

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
            #Modification of Jimmy's method, write all responses we get from arduino to firebase. Firebase then sends it to clients via FCM.
            #dataRead = arduino.readline()
            from firebase import firebase
            firebase = firebase.FirebaseApplication('linktosmarthouse', None) 
            result = firebase.patch('/categoryinfirebase',{'Response':#dataRead}) 
            print(result)


   
     

    #Method to detect a fire, then write it to some table in Firebase. This will only work good if its possible to write/read from arduino through another port other than 9600
    ''' Not used
    def update_onFire():
        while True:
         #arduino.write(str.encode(19))  Write 19 to look if its burning in house or not, this should possible be writing through a different port than the other 9600 to avoid collisions with port 9600.                                                
         #dataRead = arduino.readline() Read the response from arduino which will be "Burning or not burning"
         if dataRead is 'FIRE!!':
          from firebase import firebase
          firebase = firebase.FirebaseApplication('linktosmarthousedatabase', None)
          result = firebase.patch('/whatevernameofcategory',{'Fire':dataRead})
          time.sleep(1000)
          '''
      

      




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
