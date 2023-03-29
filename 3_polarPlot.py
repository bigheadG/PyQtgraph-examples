import sys
import math
import polarUI as pui
from PyQt5 import QtGui, QtWidgets, QtCore
import random
from threading import Thread


def update():
	print("============update============")
	win.scatterSeries.clear()
	for value in range(1, 30):
		win.scatterSeries.append(value, random.random()*20)


def uartThread(name):
	while True:
		print("=========uart Thread=========")


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = pui.MyPolarWindow()
	win.show()

	#scheduler
	t = QtCore.QTimer()
	t.timeout.connect(update)
	t.start(150) #update period = 200ms 
	t.start()
	
	#uart Thread
	thread1 = Thread(target = uartThread, args =("UART",))
	thread1.setDaemon(True)
	thread1.start()
	
	sys.exit(app.exec_())


 
