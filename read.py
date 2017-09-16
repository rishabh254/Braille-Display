import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def playAudio(i):
	pygame.mixer.init()
	pygame.mixer.music.load(str(i) + ".wav")
	pygame.mixer.music.play()

def printA():
	playAudio(1)
	blink([11])

def printB():
	playAudio(2)
	blink([11,12])

def printC():
	playAudio(3)
	blink([11,15])

def printD():
	playAudio(4)
	blink([11,15,16])

def printE():
	playAudio(5)
	blink([11,16])

def printF():
	playAudio(6)
	blink([11,12,15])

def printG():
	playAudio(7)
	blink([11,12,15,16])

def printH():
	playAudio(8)
	blink([11,12,16])

def printI():
	playAudio(9)
	blink([12,15])

def printJ():
	playAudio(10)
	blink([12,15,16])

def printK():
	playAudio(11)
	blink([11,13])

def printL():
	playAudio(12)
	blink([11,12,13])

def printM():
	playAudio(13)
	blink([11,13,15])

def printN():
	playAudio(14)
	blink([11,13,15,16])

def printO():
	playAudio(15)
	blink([11,13,16])

def printP():
	playAudio(16)
	blink([11,12,13,15])

def printQ():
	playAudio(17)
	blink([11,12,13,15,16])

def printR():
	playAudio(18)
	blink([11,12,13,16])

def printS():
	playAudio(19)
	blink([12,13,15])

def printT():
	playAudio(20)
	blink([12,13,15,16])

def printU():
	playAudio(21)
	blink([11,13,18])

def printV():
	playAudio(22)
	blink([11,12,13,18])

def printW():
	playAudio(23)
	blink([12,15,16,18])

def printX():
	playAudio(24)
	blink([11,13,15,18])

def printY():
	playAudio(25)
	blink([11,13,15,16,18])

def printZ():
	playAudio(26)
	blink([11,13,16,18])

def blink(inp):
	for i in inp:
		GPIO.setup(i,GPIO.OUT)
		GPIO.output(i,GPIO.HIGH)

	time.sleep(2)
	for i in inp:
		GPIO.output(i,GPIO.LOW)

text = "abcdefghijklmnopqrstuvwxyz"
text="i am a girl"
for char in text:
	if char=='a':
		printA()
	elif char==' ':
                time.sleep(2)
	elif char=='b':
		printB()
	elif char=='c':
		printC()
	elif char=='d':
		printD()
	elif char=='e':
		printE()
	elif char=='f':
		printF()
	elif char=='g':
		printG()
	elif char=='h':
		printH()
	elif char=='i':
		printI()
	elif char=='j':
		printJ()
	elif char=='k':
		printK()
	elif char=='l':
		printL()
	elif char=='m':
		printM()
	elif char=='n':
		printN()
	elif char=='o':
		printO()
	elif char=='p':
		printP()
	elif char=='q':
		printQ()
	elif char=='r':
		printR()
	elif char=='s':
		printS()
	elif char=='t':
		printT()
	elif char=='u':
		printU()
	elif char=='v':
		printV()
	elif char=='w':
		printW()
	elif char=='x':
		printX()
	elif char=='y':
		printY()
	elif char=='z':
		printZ()
