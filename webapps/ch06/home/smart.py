from flask import Flask
from flask import request
from flask import render_template
import RPi.GPIO as GPIO
import signal
import time

Pin_LED = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin_LED, GPIO.OUT, initial=GPIO.LOW)

def Terminate(n, p):
	GPIO.cleanup()
	print("웹 서비스를 종료합니다...")
	exit()

signal.signal(signal.SIGINT, Terminate)

app = Flask(__name__)

@app.route("/")
def Start():
	return render_template("index.html")

@app.route("/led/on")
def led_on():
	try:
		GPIO.output(Pin_LED, GPIO.HIGH)
		return "ok"
	except:
		return "FAIL"

@app.route("/led/off")
def led_off():
	try:
		GPIO.output(Pin_LED, GPIO.LOW)
		return "ok"
	except:
		return "FAIL"


@app.route("/led/blink")
def led_blink():
	try:
		for i in range(10):
			GPIO.output(Pin_LED, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(Pin_LED, GPIO.LOW)
			time.sleep(0.1)
		return "ok"
	except:
		return "FAIL"

@app.route("/song")
def song():
	try:
		p.start(10)
		for fr in Frq:
			p.ChangeFrequency(fr)
			time.sleep(speed)
		p.stop()
		return "ok"
	except:
		return "FAIL"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
