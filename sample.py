import serial
import time
import socket
#port pointing to the arduino
port = '/dev/ttyACM0'

# create and bind a socket to communicate with firebase
s = socket.socket()
host = "localhost"
socketPort = 2004  # Reserve a port for your service.
s.bind((host, socketPort))
# connect to the arduino port
arduino = serial.Serial(port, 9600)


print(arduino.readline())
while 1:
    # listen to the input from firebase
    s.listen(1)
    c, addr = s.accept()
    print("Got connection", addr)

    # read input from the socket
    length_of_message = int.from_bytes(c.recv(2), byteorder='big')
    msg = c.recv(length_of_message).decode("UTF-8")
    print(msg)

    # interpret the message received
    inputFromBase = msg.encode('UTF-8')
    response_From_Arduino = ''
    if b'1' in inputFromBase:
        arduino.write(b'<1>')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'2' in inputFromBase:
        arduino.write(b'<2>')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'3' in inputFromBase:
        arduino.write(b'<3>')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'4' in inputFromBase:
        arduino.write(b'<4>')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'5' in inputFromBase:
        arduino.write(b'5')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'6' in inputFromBase:
        arduino.write(b'6')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'7' in inputFromBase:
        arduino.write(b'7')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'8' in inputFromBase:
        arduino.write(b'8')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'9' in inputFromBase:
        arduino.write(b'9')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'10' in inputFromBase:
        arduino.write(b'10')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'11' in inputFromBase:
        arduino.write(b'11')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)
    if b'12' in inputFromBase:
        arduino.write(b'12')
        response_From_Arduino = arduino.readline()
        print(response_From_Arduino)

    message_to_send = b'Received ' + response_From_Arduino
    c.send(len(message_to_send).to_bytes(2, byteorder='big'))
    c.send(message_to_send)
    # close the socket
    c.shutdown(1)
    c.close()
    time.sleep(1)

