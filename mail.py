import time
import grovepi
import smtplib
import subprocess
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from grove_rgb_lcd import *
import random
import sys
from threading import Thread
import collectheart

# coding=utf-8
# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND

class Mail(Thread):
    def __init__(self,message1,message2):        
	Thread.__init__(self)
        #initialisation des entrees sorties self pour dire que si on les appels c'est celle de ce programme
        self.button1 = 3
        self.button2 = 4
	self.button3 = 2
        self.buzzer = 7
        grovepi.pinMode(self.buzzer,"OUTPUT")
        grovepi.pinMode(self.button1,"INPUT")
        grovepi.pinMode(self.button2,"INPUT")
	grovepi.pinMode(self.button3,"INPUT")
        self.msg = MIMEMultipart()
        self.message1 = message1
	self.message2 = message2
        self.mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        try:
            setRGB(255,75,0)
            setText("Bonjour,\nDemarrage BOX")
            time.sleep(5)

            setRGB(10,10,10)
            setText("BOX ACITVE")
        except IOError:
            setText("IOError")

    def run(self):
        while True:
            try:
                if (grovepi.digitalRead(self.button1)):
			self.mailserver = smtplib.SMTP('smtp.gmail.com', 587)
			self.msg['From'] = 'fasoandrebourrat@gmail.com'
			self.msg['To'] = 'mathis.bourrat@etu.umontpellier.fr'
			self.msg['Subject'] = 'urgence'
			self.msg.attach(MIMEText(self.message1))
			self.mailserver.ehlo()
                        self.mailserver.starttls()
                        self.mailserver.ehlo()
                        self.mailserver.login('fasoandrebourrat@gmail.com', 'depIG_2018')
                        self.mailserver.sendmail('fasoandrebourrat@gmail.com', 'mathis.bourrat@etu.umontpellier.fr', self.msg.as_string())
                        self.mailserver.quit()
                        setRGB(0,255,0)
                        setText("MEDECIN \n CONTACTEE")
                        grovepi.digitalWrite(self.buzzer,1)
                        time.sleep(0.5)
                        grovepi.digitalWrite(self.buzzer,0)
                        time.sleep(10)
                        setRGB(10,10,10)
                        setText("BOX ACITVE")

                if (grovepi.digitalRead(self.button2)):
                        self.mailserver = smtplib.SMTP('smtp.gmail.com', 587)
                        self.msg['From'] = 'fasoandrebourrat@gmail.com'
                        self.msg['To'] = 'bourratmathis@gmail.com'
                        self.msg['Subject'] = 'visite'
                        self.msg.attach(MIMEText(self.message2))
                        self.mailserver.ehlo()
                        self.mailserver.starttls()
                        self.mailserver.ehlo()
                        self.mailserver.login('fasoandrebourrat@gmail.com', 'depIG_2018')
                        self.mailserver.sendmail('fasoandrebourrat@gmail.com', 'bourratmathis@gmail.com',self.msg.as_string())
                        self.mailserver.quit()
                        setRGB(0,255,0)
                        setText("FAMILLE \n CONTACTEE")
                        grovepi.digitalWrite(self.buzzer,1)
                        time.sleep(0.5)
                        grovepi.digitalWrite(self.buzzer,0)
                        time.sleep(10)
                        setRGB(10,10,10)
                        setText("BOX ACITVE")

		if (grovepi.digitalRead(self.button3)):
			collectheart.showfreq()
            except IOError:
                print ("Error")


