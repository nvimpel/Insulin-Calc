import pandas as pd
dataFile = pd.read_csv('FileName',sep=',')

#set day value to first day of the list
day = 0
dayPhase = 0
controlSugarValue = 24.4

#glucose array with 3X control values for functionality control
MorningList = [4.04,0,4]
LunchList = [4.04,0,4]
EveningList = [4.04,0,4]
NigthList = [4.04,0,4]

#insulin arrays with 3X control values
MorningInsulin = [1,1,1]
LunchInsulin = [1,1,1]
EveningInsulin = [1,1,1]
NigthInsulin = [1,1,1]

#Day array with control values
dayArray = [6,5,4]

#Insulin variable + median Insulin value
Insulin = 15

#the range of the data input list
BegID = 1
EndID = 1234567

MMin = 24.4
LMin = 24.4
EMin = 24.4
NMin = 24.4
SugMin = 24.4

for i in range(BegID, EndID):
    if dataFile.values[i][0] == day:
        if dayPhase == DetermineDayPhase(dataFile.values[i][2]):
            if ConvertValue(dataFile.values[i][4]) < SugMin:
                SugMin = ConvertValue(dataFile.values[i][4])
        
def DetermineDayPhase(hour):
    if hour >= 6 and hour <=9:
        return(1)
    if hour >= 11 and hour <=14:
        return(2)
    if hour >= 16 and hour <=19:
        return(3)
    if hour >= 21 and hour <=23:
        return(4)
    return(0);

def ConvertValue(inputV)
    if inputV == 'Vysoké':
        return(24.4)
    elif inputV == 'Nízke':
        return(2.2)
    return(inputV)
    
    

def InsulinAssign():
