from Tkinter import *
from getIp import *
import os

root = Tk()
root.geometry("400x120")

def switchToLCD():
	os.system("cd /home/pi/LCD-show && ./LCD32-show")
def switchToHDMI():
        os.system("cd /home/pi/LCD-show && ./LCD-hdmi")
def close():
	root.destroy()
def updateIpVar():
	ipVar.set(get_ip_address('wlan0') + "\n" + get_ip_address('wlan1'))

topFrame = Frame(root)
LCDbutton = Button(topFrame, text="LCD", command = switchToLCD)
HDMIbutton = Button(topFrame, text="HDMI", command = switchToHDMI)
CLOSEbutton = Button(topFrame, text="Close", command = close)

bottomFrame = Frame(root)
ipVar = StringVar()
IPbutton = Button(bottomFrame, textvariable=ipVar, command = updateIpVar)
ipVar.set('Refresh IP')

LCDbutton.config(height=3, width=5)
HDMIbutton.config(height=3, width=5)
CLOSEbutton.config(height=3, width=5)
IPbutton.config(height=3, width=10)

topFrame.pack(side="top")
LCDbutton.pack(side='left')
HDMIbutton.pack(side='left')
CLOSEbutton.pack(side='left')

bottomFrame.pack(side='bottom')
IPbutton.pack(side='left')

root.mainloop()
