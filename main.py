import time
from os import system, name


#3600 seconds in an hour.
#60 seconds in a minute.
#1 second in a second 
#86400 seconds in a day (24 hours)


def clear():
   # for windows
   if name == 'nt':
    _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')



def convertToTime(totalseconds):
   hours = int(totalseconds)//3600
   minutes = (int(totalseconds) - (3600*hours))//60
   seconds = int(totalseconds) - (3600*hours)-(minutes*60)
   return hours, minutes, seconds
   
   
   
def convertToSeconds(hrs, mins, secs):
  convertedSeconds = (int(hrs)*3600)+(int(mins)*60)+int(secs)
  return convertedSeconds
   
   
def printTime(hrs,mins,secs):
  if int(hrs) < 10: hrs = "0" + str(hrs)
  if int(mins) < 10: mins = "0" + str(mins)
  if int(secs) < 10: secs = "0" + str(secs)

def calculateDifference(totalsecs1,totalsecs2):

    differenceSecs = totalsecs2 - totalsecs1

    
    return differenceSecs
      



clear() #Clear the screen at the start


#MODE SELECTION-------------

modeCorrect = False
while modeCorrect == False:
    try:
        mode = int(input("Select the mode you would like to use: [1 or 2]\n[1]: Calculate difference between two given time periods.\n[2]: Calculate the time after adding another amount of time.\n>"))
        if mode == 1 or mode == 2:
            modeCorrect = True
        else: heheyeahboi = int('hhehehe') #Code which will result in an error, therefore triggering the code in the 'except' part
    except:
       clear()
       print("Please input a number between 1 or 2.")
       time.sleep(1.5)
       clear()
       modeCorrect = False

#----------------------
       
if mode == 1: #Calculating time between two given times
   clear()
   try:
    hour1 = int(input("Time 1\nHour [00-23]: "))
    minute1 = int(input("Minute [00-59]: "))
    sec1 = int(input("Second [00-59]: "))
    if minute1 > 59 or minute1 < 0 or sec1 < 0 or sec1 > 59 or hour1 < 0 or hour1 > 23:
        heheyeahboi = int('hhehehe') #trigger the except part.
        
    totalsecs1 = convertToSeconds(hour1,minute1,sec1)
    if hour1 < 10: hour1str = "0" + str(hour1)
    else: hour1str = str(hour1)
    if minute1 < 10: minute1str = "0"+str(minute1)
    else: minute1str = str(minute1)#
    if sec1 < 10: sec1str = "0" + str(sec1)
    else: sec1str = str(sec1)
    time1str = hour1str+":"+minute1str+":"+sec1str
    clear()
        
    print("Time 1: "+time1str+"\n")
    hour2 = int(input("Time 2\nHour [00-23]: "))
    minute2 = int(input("Minute [00-59]: "))
    sec2 = int(input("Second [00-59]: "))
    if minute2 > 59 or minute2 < 0 or sec2 < 0 or sec2 > 59 or hour2 < 0 or hour2 > 23:
        heheyeahboi = int('hhehehe') #trigger the except part.
        
    totalsecs2 = convertToSeconds(hour2,minute2,sec2)
    if hour2 < 10: hour2str = "0" + str(hour2)
    else: hour2str = str(hour2)
    if minute2 < 10: minute2str = "0"+str(minute2)
    else: minute2str = str(minute2)
    if sec2 < 10: sec2str = "0" + str(sec2)
    else: sec2str = str(sec2)
    time2str = hour2str+":"+minute2str+":"+sec2str

    clear()
    print("Calculating...")
    print("Time 1: "+time1str)
    time.sleep(1)
    print("Time 2: "+time2str)
    time.sleep(1)
        
    finalCalculationSecs = calculateDifference(totalsecs1,totalsecs2)
    finalHour, finalMinute, finalSeconds = convertToTime(finalCalculationSecs)
        
    print("The difference in the time "+time1str+" and "+time2str+" is "+ str(finalHour) + " hours, "+ str(finalMinute)+" minutes, and "+str(finalSeconds)+" seconds.")
    if finalCalculationSecs < 0: print("Time 2 wasn't meant to be smaller than time 1, so we just gave you the negative value...")




   except:
      print("Error. Restart the project and make sure to input integer values between the given ranges.")



elif mode == 2:
   origHour = int(input("Input the hour of the time to add from [00-23]: "))
   origMin = int(input("Input the minute of the time to add from [00-59]: "))
   origSec = int(input("Input the second of the time to add from [00-59]: "))
   if origHour < 10: origHourStr = "0"+str(origHour)
   else: origHourStr = str(origHour)
   if origMin < 10: origMinStr = "0"+str(origMin)
   else: origMinStr = str(origMin)
   if origSec < 10: origSecStr = "0"+str(origSec)
   else: origSecStr = str(origSec)
   origTimeStr = origHourStr+":"+origMinStr+":"+origSecStr

   origTimeTotalSecs = convertToSeconds











       





