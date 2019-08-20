#prerequisites - PySeral library


import datetime as dt
import serial

comPort = input('what COM port is your Arduino connected to? ')
ser = serial.Serial(comPort,115200)

timer = dt.datetime.now()

timeList = (timer.year, timer.month, timer.day, timer.hour, timer.minute, timer.second)
#can also add timer.microsecond, needs setup on Arduino
msg = 'y '+str(timeList[0])+' mo '+str(timeList[1])+' d ' +str(timeList[2])+' h ' +str(timeList[3])+' mi '+str(timeList[4])+' s ' +str(timeList[5])

ser.write(msg.encode('utf-8'))
print('set time: ' + msg)
ser.close()
#quit()
