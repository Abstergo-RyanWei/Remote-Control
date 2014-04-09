import win32com.client
import time
import serial
shell=win32com.client.Dispatch("WScript.Shell")
arduinos=['COM5','COM6','COM7','COM8','COM9','COM10','COM11',
'COM12','COM13','COM14','COM15','COM16','COM17','COM18','COM19','COM20']
for device in arduinos:
    try:
        print "Connecting...",device
        arduino = serial.Serial(device, 9600)
        break
    except:
        print "Failed to connect on",device

while True:
    line=arduino.read();
    #print line
    if line=="a":
        shell.sendKeys("{ }")
