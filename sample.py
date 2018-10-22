import serial
import time
import os

port = '/dev/ttyACM0'

# connect to the port
arduino = serial.Serial(port, 9600)

print(arduino.readline())
while 1:
	inputFromBase = b'1' #pipeFromBase.readline()
	if b'1' in inputFromBase:
		arduino.write(b'<1>')
		print(arduino.readline())
	if b'2' in inputFromBase:
		arduino.write(b'<2>')
		print(arduino.readline())
	if b'3' in inputFromBase:
		arduino.write(b'<3>')
		print(arduino.readline())
	if b'4' in inputFromBase:
		arduino.write(b'<4>')
		print(arduino.readline())
	if b'5' in inputFromBase:
		arduino.write(b'<5>')
		print(arduino.readline())
	if b'6' in inputFromBase:
		arduino.write(b'<6>')
		print(arduino.readline())
	if b'7' in inputFromBase:
		arduino.write(b'<7>')
		print(arduino.readline())
	if b'8' in inputFromBase:
		arduino.write(b'<8>')
		print(arduino.readline())
	if b'9' in inputFromBase:
		arduino.write(b'<9>')
		print(arduino.readline())
	if b'10' in inputFromBase:
		arduino.write(b'<10>')
		print(arduino.readline())
	if b'11' in inputFromBase:
		arduino.write(b'<11>')
		print(arduino.readline())
	if b'12' in inputFromBase:
		arduino.write(b'<12>')
		print(arduino.readline())
	time.sleep(1)



