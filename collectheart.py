import serial
import requests
import time
import grovepi
from grove_rgb_lcd import *
import sys
from threading import Thread


ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600)

def showfreq():
	count = 0
	while count<5:
		line=ser.readline()
		setText("pulse: " + line)
		time.sleep(2)
		count += 1
	setText("BOX active")


class sendFrequence(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600)

	def run(self):
        	while True:
                	line = self.ser.readline()
			print(line)
                	data = {"entry.1641621488":line}
                	requests.post("https://docs.google.com/forms/d/1gfiHars_1bIEvNVcMuJevnSkfyzPsWiM6mKFWnhEkEY/formResponse?", data =data)
                	time.sleep(5)


