import pandas as pd
df = pd.read_csv('Converted102024.csv',sep=',')

#set day values to first date of the list
day = 30
lSug = 24.4
#glucose list with 3 control values
lSugListM = [4.04,0,4]
lSugListL = [4.04,0,4]
lSugListE = [4.04,0,4]
lSugListN = [4.04,0,4]
#insulin list with 3 control values
InM = [1,1,1]
InL = [1,1,1]
InE = [1,1,1]
InN = [1,1,1]
#median control value
ins = 15;
#day list with 3 control values
dayList =  [5,4,3]
#minmax values
minV = 2;
maxV = 32997;


def setTimeScale(set, lowIn, midIn, highIn, timeIn, timeOut):
    day = 30
    for i in range(2, maxV):
        if df.values[i][0] == day:
            hour = df.values[i][2]
            if hour >= timeIn and hour <= timeOut:
                aSug = df.values[i][4]
                if aSug == 'Vysoké':
                    lSug = lSug
                elif aSug == 'Nízke':
                    lSug = 2.2
                elif float(aSug) < lSug:
                    lSug = float(aSug)
        
        else:
            if lSug < 7:
                ins = lowIn
            elif lSug > 15:
                ins = highIn
            else:
                ins = midIn
            
            if set == 1:
                InM.append(ins)
                lSugListM.append(lSug)
            elif set == 2:
                InL.append(ins)
                lSugListL.append(lSug)
            elif set == 3:
                InE.append(ins)
                lSugListE.append(lSug)
            elif set == 4:
                InN.append(ins)
                lSugListN.append(lSug)

            dayList.append(day)
            lSug = 24.4
            if day > 31:
                day = 1
            else:
                day = day + 1
        
            

#[time][lowIn][midIn][highIN][timeStart][timeEnd]
setTimeScale(1,7,9,11,6,9)
setTimeScale(2,16,16,17,11,14)
setTimeScale(3,16,17,18,16,19)
setTimeScale(4,18,18,18,21,23)


#for j in lSugList:
        #print(j)
#print(len(lSugListM),len(lSugListL),len(lSugListE),len(lSugListN))


dict = {'day': dayList, 'Morning': lSugListM, 'Lunch': lSugListL, 'Evening': lSugListE, 'Night': lSugListN, 'MorIns': InM, 'LunIns': InL, 'EveIns': InE, 'NightIns': InN}
export = pd.DataFrame(dict)
export.to_csv('FinalExportData1024_1.csv')
print('Done')
            



        
    


#print(df.to_string())

