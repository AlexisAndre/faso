import requests
import serial

ser = serial.Serial(port = '/dev/ttyACM0',baudrate = 9600)
while True:
	Line = ser.readline()
	Value = int(Line)
	data = {"entry.1326754062 " : Value}
	requests.post("https://docs.google.com/forms/d/189zWuvrzEwNFvSo86agxLt8At3MJUgpjEc-I7odjy3A/formResponse?", data =data)
