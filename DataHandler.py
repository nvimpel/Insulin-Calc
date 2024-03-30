import pandas as pd
df = pd.read_csv('2Converted022024.csv',sep=',')

#set day values to first date of the list
day = 3
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
maxV = 4444;

#set the range based on size of spreadsheet
for i in range(2, maxV):
    if df.values[i][0] == day:
        hour = df.values[i][2]
        if hour >= 6 and hour <=9:
            aSug = df.values[i][4]
            if aSug == 'Vysoké':
                lSug = lSug
            elif aSug == 'Nízke':
                lSug = 2.2
            elif lSug > float(aSug):
                lSug = float(aSug)
                
    
            
    else:
        if lSug < 7:
            ins = 12
        elif lSug > 12:
            ins = 14
        else:
            ins = 12
        InM.append(ins)
            
        

        lSugListM.append(lSug)
        dayList.append(day)
        lSug = 24.4
        if day > 31:
            day = 1
        else:
            day = day + 1
            
day = 3
for i in range(2, maxV):
    if df.values[i][0] == day:
        hour = df.values[i][2]
        if hour >= 11 and hour <=14:
            aSug = df.values[i][4]
            if aSug == 'Vysoké':
                lSug = lSug
            elif aSug == 'Nízke':
                lSug = 2.2
            elif lSug > float(aSug):
                lSug = float(aSug)
                
    
            
    else:
        if lSug < 7:
            ins = 15
        elif lSug > 15:
            ins = 18
        else:
            ins = 16
        InL.append(ins)

        lSugListL.append(lSug)
        
        lSug = 24.4
        if day > 31:
            day = 1
        else:
            day = day + 1
            
day = 3        
for i in range(2, maxV):
    if df.values[i][0] == day:
        hour = df.values[i][2]
        if hour >= 16 and hour <=19:
            aSug = df.values[i][4]
            if aSug == 'Vysoké':
                lSug = lSug
            elif aSug == 'Nízke':
                lSug = 2.2
            elif lSug > float(aSug):
                lSug = float(aSug)
                
    
            
    else:
        if lSug < 7:
            ins = 15
        elif lSug > 15:
            ins = 17
        else:
            ins = 16
        InE.append(ins)

        lSugListE.append(lSug)

        lSug = 24.4
        if day > 31:
            day = 1
        else:
            day = day + 1

day = 3
for i in range(2, maxV):
    if df.values[i][0] == day:
        hour = df.values[i][2]
        if hour >= 21 and hour <=23:
            aSug = df.values[i][4]
            if aSug == 'Vysoké':
                lSug = lSug
            elif aSug == 'Nízke':
                lSug = 2.2
            elif lSug > float(aSug):
                lSug = float(aSug)
                
    
            
    else:

        InN.append(18)
        lSugListN.append(lSug)

        lSug = 24.4
        if day > 31:
            day = 1
        else:
            day = day + 1

#for j in lSugList:
        #print(j)
#print(len(lSugListM),len(lSugListL),len(lSugListE),len(lSugListN))
dict = {'day': dayList, 'Morning': lSugListM, 'Lunch': lSugListL, 'Evening': lSugListE, 'Night': lSugListN, 'MorIns': InM, 'LunIns': InL, 'EveIns': InE, 'NightIns': InN}
export = pd.DataFrame(dict)
export.to_csv('FinalExportData0224_2.csv')
print('Done')
            



        
    


#print(df.to_string())

