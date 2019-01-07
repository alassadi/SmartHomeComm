import os
import sys 
import time
import requests, json
import queue
import threading
import random
# import serial

# port = '/dev/ttyACM0'
# arduino = serial.Serial(port, 9600)

# print(arduino.readline())

class Watcher(object):
    running = True
    refresh_milliSecond = 0.010
    
    
   

    # Constructor
    def __init__(self, watch_file, *args, **kwargs):
        self._cached_stamp = 0
        self.filename = watch_file
        self.args = args
        self.kwargs = kwargs
        
        thread = threading.Thread(target=self.checkFire, args=())
        #thread2 = threading.Thread(target=self.checkWaterLeak, args=())
        thread.daemon = True
        #thread2.daemon = True
        thread.start()
        #thread2.start()
        
        
        
        
       

    # Look for changes
    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
           

            filepath = 'C:\\Users\\robin\\Desktop\\Javascript\\tester12\\test.txt'
            f = open(filepath, 'r')
            line = f.readline()
            print(line+" sent.")
            dataRead = line
            from firebase import firebase
            firebase = firebase.FirebaseApplication('https://fir-test-7f5bd.firebaseio.com/', None)
            result = firebase.patch('/ResponseFromArduino',{'Response':'LAMP OFF'})
            print(result)

            
           

    
    def checkFire(self):
        #arduino.write(str.encode(19))
        #dataRead = arduino.readline()
        while True:
         checka = random.randint(1,101)
         if checka > 0:
          #arduino.write(str.encode(19))
          from firebase import firebase
          firebase = firebase.FirebaseApplication('https://fir-test-7f5bd.firebaseio.com/', None)
          result = firebase.patch('/ResponseFromArduino',{'Fire':checka})
          time.sleep(100)
          

    '''
    def checkWaterLeak(self):
        #arduino.write(str.encode(19))
        #dataRead = arduino.readline()
        while True:
         checka = random.randint(1,101)
         if checka > 0:
          from firebase import firebase
          firebase = firebase.FirebaseApplication('https://fir-test-7f5bd.firebaseio.com/', None)
          result = firebase.patch('/ResponseFromArduino',{'Waterleak':checka})
          time.sleep(100)
          '''
         
         
         

         
        


         

             
            
         
   # Keep watching in a loop
    def watch(self):
 
        while self.running:
            try:
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


watch_file = 'C:\\Users\\robin\\Desktop\\Javascript\\tester12\\test.txt'

# watcher = Watcher(watch_file)  # simple
watcher = Watcher(watch_file)  # also call custom action function
watcher.watch()  # start the watch going
