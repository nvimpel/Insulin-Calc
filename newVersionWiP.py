import pandas as pd
dataFile = pd.read_csv('Converted112023.csv',sep=',')

#set day value to first day of the list
day = 0
dayPhase = 'Phase'
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
EndID = 800

MMin = 24.4
LMin = 24.4
EMin = 24.4
NMin = 24.4


def main():
    day = dataFile.values[2][0];
    dayPhase = getPhase(2)
    SugMin = 24.4
    Skipped = False;
    for i in range(3, EndID):
        #check if day is the same
        if dataFile.values[i][0] == day:
            #get phase, correct sugar value, append value to array
            if getPhase(i) != getPhase(i-1) and getPhase(i) != 'Skip':
                appendValue(day, getPhase(i), SugMin)
                print(getPhase(i), 'appending...')
                dayPhase = getPhase(i)
            elif getPhase(i) == getPhase(i-1) and getPhase(i) != 'Skip':
                aSug = dataFile.values[i][4]
                if aSug == 'Vysoké':
                    SugMin = SugMin
                elif aSug == 'Nízke':
                    SugMin = 2.2
                elif SugMin > float(aSug):
                    SugMin = float(aSug)  
            
        else:
            print('New day ', day)
            dayArray.append(day)
            day = dataFile.values[i][0]
            SugMin = controlSugarValue
    
    saveData()

   
def getPhase(id):
    if dataFile.values[id][2] >= 6 and dataFile.values[id][2] <= 9:
        return 'Morning'
    elif dataFile.values[id][2] >= 10 and dataFile.values[id][2] <= 13:
        return 'Lunch'
    elif dataFile.values[id][2] >= 14 and dataFile.values[id][2] <= 17:
        return 'Evening'
    elif dataFile.values[id][2] >= 18 and dataFile.values[id][2] <= 21:
        return 'Nigth'
    else:
        return 'Skip'
    
def appendValue(day, dayPhase, SugMin):
    if dayPhase == 'Morning':
        MorningList.append(SugMin)
        MorningInsulin.append(getInsulin(dayPhase, SugMin))
    elif dayPhase == 'Lunch':
        LunchList.append(SugMin)
        LunchInsulin.append(getInsulin(dayPhase, SugMin))
    elif dayPhase == 'Evening':
        EveningList.append(SugMin)
        EveningInsulin.append(getInsulin(dayPhase, SugMin))
    elif dayPhase == 'Nigth':
        NigthList.append(SugMin)
        NigthInsulin.append(getInsulin(dayPhase, SugMin))
    else:
        print(f'Error {day} {dayPhase} {SugMin}')
    Skipped = False;
    SugMin = controlSugarValue

def getInsulin(dayPhase, SugMin):
    if dayPhase == 'Morning':
        if SugMin < 7:
            return 9
        elif SugMin > 12:
            return 12
        else:
            return 11
    elif dayPhase == 'Lunch':
        if SugMin < 7:
            return 15
        elif SugMin > 15:
            return 16
        else:
            return 16
    elif dayPhase == 'Evening':
        if SugMin < 7:
            return 15
        elif SugMin > 12:
            return 16
        else:
            return 16
    elif dayPhase == 'Nigth':
        return 18
    else:
        print('Error')

def saveData():
    dayArray.append(day)
    print(len(dayArray), ' ', len(MorningList), ' ', len(LunchList), ' ', len(EveningList), ' ', len(NigthList), ' ', len(MorningInsulin), ' ', len(LunchInsulin), ' ', len(EveningInsulin), ' ', len(NigthInsulin))
    print('Saving data...')
    dict = {'day': dayArray, 'Morning': MorningList, 'Lunch': LunchList, 'Evening': EveningList, 'Night': NigthList, 'MorIns': MorningInsulin, 'LunIns': LunchInsulin, 'EveIns': EveningInsulin, 'NightIns': NigthInsulin}
    export = pd.DataFrame(dict)
    export.to_csv('NewPYExport.csv')
    print('Done')

#def beautifyData():
    

if __name__ == "__main__":
    main()