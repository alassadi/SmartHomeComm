import os
import sys 
import time

#port = '/dev/ttyACM0'

# arduino = serial.Serial(port, 9600)

#print(arduino.readline())

class Watcher(object):
    running = True
    refresh_delay_secs = 1

    # Constructor
    def __init__(self, watch_file, call_func_on_change=None, *args, **kwargs):
        self._cached_stamp = 0
        self.filename = watch_file
        self.call_func_on_change = call_func_on_change
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
            if self.call_func_on_change is not None:
                self.call_func_on_change(*self.args, **self.kwargs)




    # Keep watching in a loop        
    def watch(self):
        while self.running: 
            try: 
                # Look for changes
                time.sleep(self.refresh_delay_secs) 
                self.look() 
            except KeyboardInterrupt: 
                print('\nDone') 
                break 
            except FileNotFoundError:
                # Action on file not found
                pass
            except: 
                print('Unhandled error: %s' % sys.exc_info()[0])

# Call this function each time a change happens
def custom_action(text):
    print(text)

#watch_file = 'C:\\Users\\Robin\\Desktop\\tester12\\test.txt'
watch_file = r'./test.txt'

# watcher = Watcher(watch_file)  # simple
watcher = Watcher(watch_file, custom_action, text='File changed')  # also call custom action function
watcher.watch()  # start the watch going