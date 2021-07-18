from flask import Flask
from flask import request
from flask import render_template
import RPi.GPIO as GPIO
import signal
import time
import serial

ObjSerial = serial.Serial('/dev/ttyACM0', 9600)

def Terminate(n, p):
	GPIO.cleanup()
	print("웹 서비스를 종료합니다...")
	exit()

signal.signal(signal.SIGINT, Terminate)

app = Flask(__name__)

@app.route("/")
def Start():
	return render_template("index.html")

@app.route("/LED1")
def LED1():
	try:
		ObjSerial.write('1'.encode())
		return "OK"
	except:
		return "FAIL"

@app.route("/LED2")
def LED2():
	try:
		ObjSerial.write('2'.encode())
		return "OK"
	except:
		return "FAIL"

@app.route("/LED3")
def LED3():
	try:
		ObjSerial.write('3'.encode())
		return "OK"
	except:
		return "FAIL"
@app.route("/song")
def song():
	try:
		ObjSerial.write('4'.encode())
		return "OK"
	except:
		return "FAIL"
@app.route("/temp")
def temp():
	try:
		ObjSerial.write('5'.encode())
		temp=ObjSerial.readline().decode()
		return temp
	except:
		return "FAIL"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
