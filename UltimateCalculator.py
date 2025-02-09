import pandas as pd
def main():
    data = loadData()
    print('Data loaded')
    maxValue = getEndValue()
    day = data[[2][0]]
    month = data[[2][1]]
    createArrays(day, month, maxValue, data);

def createArrays(day, month, maxValue, data):
    for i in range(3, maxValue):
        if data.values[i][0] == day:
            hour = data.values[i][2]
            if hour >= 16 and hour <=19:
                aSug = data.values[i][4]
                if aSug == 'Vysoké':
                    lSug = lSug
                elif aSug == 'Nízke':
                    lSug = 2.2
                elif lSug > float(aSug):
                    lSug = float(aSug)
        
def getEndValue():
    print('write the end value')
    return input()
def loadData():
    print('write the file name')
    data = pd.read_csv(input(), sep=',')
    print(data)
    return data

if __name__ == "__main__":
    main()
