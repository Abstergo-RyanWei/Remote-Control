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

while not (arduino.inWaiting()>0):
    time.sleep(0.0001)

while True:
    send=arduino.read()
    if send=='c':
        print "Let's go crazy!"
        arduino.flushInput();
        while (not arduino.inWaiting()):
            shell.sendKeys("{DOWN}")
            time.sleep(0.001)
            shell.sendKeys("{LEFT}")
            time.sleep(0.001)
            shell.sendKeys("{DOWN}")
            time.sleep(0.001)
            shell.sendKeys("{RIGHT}")
            time.sleep(0.001)

    else:
        if send=='u':
            shell.sendKeys("{UP}")
            print "You went up."
        elif send=='d':
            shell.sendKeys("{DOWN}")
            print "You went down."
        elif send=='l':
            shell.sendKeys("{LEFT}")
            print "You went left."
        elif send=='r':
            shell.sendKeys("{RIGHT}")
            print "You went right."
        elif send=='n':
            print "Let's go normal."
        else:
            print "Oops!There are something wrong with the program,hehe!"
        arduino.flushInput();
        while (not arduino.inWaiting()):
            time.sleep(0.001)
    
    
    
