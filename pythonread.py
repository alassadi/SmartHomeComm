import os
import sys 
import time

#port = '/dev/ttyACM0'

# arduino = serial.Serial(port, 9600)

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

    
    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
            f = open(r'C:\\Users\\Robin\\Desktop\\kk.txt', 'r')
            line = f.readline()
            inputFromBase = line
            print(inputFromBase)
            if inputFromBase is '1':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('1 was sent to Arduino')
            if inputFromBase is '2':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('2 was sent to Arduino')
            if inputFromBase is '3':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('3 was sent to Arduino')
            if inputFromBase is '4':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('4 was sent to Arduino')
            if inputFromBase is '5':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('5 was sent to Arduino')
            if inputFromBase is '6':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('6 was sent to Arduino')
            if inputFromBase is '7':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('7 was sent to Arduino')
            if inputFromBase is '8':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('8 was sent to Arduino')
            if inputFromBase is '9':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('9 was sent to Arduino')
            if inputFromBase == '10':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('10 was sent Arduino')
            if inputFromBase == '11':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('11 was sent to Arduino')
            if inputFromBase == '12':
            	#arduino.write(b'<1>')
            	#response_From_Arduino = arduino.readline()
            	#print(response_From_Arduino)
            	print('12 was sent to Arduino')
          




       
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
                print('No file found')
                pass
            except: 
                print('Unhandled error: %s' % sys.exc_info()[0])




watch_file = 'C:\\Users\\Robin\\Desktop\\kk.txt'


watcher = Watcher(watch_file) 
watcher.watch()  
